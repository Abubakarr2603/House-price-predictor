import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="House Price Predictor", page_icon="🏡", layout="centered")

st.title("🏡 Real Estate Price Predictor")
st.write("Enter the property details below to get an instant valuation.")

# 2. UI Layout (Two columns for a clean look)
col1, col2 = st.columns(2)

with col1:
    overall_qual = st.slider("Overall Quality (1-10)", min_value=1, max_value=10, value=7)
    indoor_area = st.number_input("Total Indoor Area (sq ft)", min_value=500.0, max_value=10000.0, value=2200.5)
    year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2005)
    lot_area = st.number_input("Lot Area (sq ft)", min_value=1000.0, max_value=50000.0, value=8500.0)

with col2:
    garage_cars = st.number_input("Garage Size (Cars)", min_value=0, max_value=5, value=2)
    outdoor_area = st.number_input("Total Outdoor Area (sq ft)", min_value=0.0, max_value=3000.0, value=250.0)
    kitchen_qual = st.selectbox("Kitchen Quality", options=["Ex", "Gd", "TA", "Fa", "Po"], index=1)
    bldg_type = st.selectbox("Building Type", options=["1Fam", "2fmCon", "Duplex", "TwnhsE", "Twnhs"], index=0)

# 3. Prediction Button
if st.button("Predict Price", type="primary", use_container_width=True):
    # Package the UI inputs into the JSON payload
    payload = {
        "OverallQual": overall_qual,
        "TotalIndoorArea": indoor_area,
        "YearBuilt": year_built,
        "LotArea": lot_area,
        "GarageCars": garage_cars,
        "TotalOutdoorArea": outdoor_area,
        "KitchenQual": kitchen_qual,
        "BldgType": bldg_type
    }
    
    try:
        # Send the POST request to your live Oracle server
        response = requests.post("http://158.101.234.115:8001/predict", json=payload)
        
        if response.status_code == 200:
            price = response.json()["predicted_price"]
            st.success(f"Estimated Property Value: **${price:,.2f}**")
        else:
            st.error(f"Error from server: {response.text}")
            
    except requests.exceptions.RequestException:
        st.error("Failed to connect to the backend. Ensure your Oracle server is running and port 8001 is open.")