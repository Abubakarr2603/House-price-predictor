from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Initialize the API
app = FastAPI(title="House Price Predictor API")

# 2. Load the machine learning artifacts into memory
try:
    model = joblib.load('rf_house_model.joblib')
    encoder = joblib.load('house_encoder.joblib')
    model_columns = joblib.load('model_columns.joblib')
except Exception as e:
    print(f"Error loading files. Make sure .joblib files are in the same folder. {e}")

# 3. Define the expected dashboard inputs (Keep this to the top 10-15 features)
class HouseData(BaseModel):
    OverallQual: int
    TotalIndoorArea: float
    YearBuilt: int
    LotArea: float
    GarageCars: int
    TotalOutdoorArea: float
    # Example text categories to show the encoder working:
    KitchenQual: str = "TA"  
    BldgType: str = "1Fam"

@app.post("/predict")
def predict_price(house: HouseData):
    try:
        # 1. Convert the JSON input directly into a 1-row Pandas DataFrame
        user_input = house.model_dump()
        df = pd.DataFrame([user_input])
        
        # 2. Ask the encoder EXACTLY which text columns it memorized during training
        expected_text_cols = encoder.feature_names_in_
        
        # 3. Add those missing text columns to our dashboard data, filled with 'Missing'
        for col in expected_text_cols:
            if col not in df.columns:
                df[col] = 'Missing'
                
        # 4. Apply the encoder using its perfectly matched column list
        encoded_array = encoder.transform(df[expected_text_cols])
        encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(expected_text_cols))
        
        # 5. Swap the old text columns for the new mathematical ones
        df = df.drop(expected_text_cols, axis=1)
        df = pd.concat([df, encoded_df], axis=1)
        
        # 6. Reindex to align the final numerical columns for the Random Forest
        df = df.reindex(columns=model_columns, fill_value=0)
        
        # 7. Predict and return
        prediction = model.predict(df)[0]
        return {"predicted_price": round(prediction, 2)}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))