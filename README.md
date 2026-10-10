# 🏡 Full-Stack House Price Predictor

An end-to-end Machine Learning production service built with **Python**, **Scikit-Learn**, **FastAPI**, and **Streamlit**. The entire application is containerized using **Docker** for continuous cloud deployment.

This project takes raw real estate data from the Kaggle House Prices competition, cleans and engineers optimized features, trains a **Random Forest Regressor** model achieving an $R^2$ score of **\~0.88**, and exposes a production-ready REST API connected to an interactive web dashboard.

## 🚀 Project Highlights & Architecture

* **Machine Learning Model:** Random Forest Regressor trained on optimized house features.
* **Feature Engineering:** Combined redundant architectural inputs into intuitive super-features:
  * `TotalIndoorArea`: Aggregates above-ground living space (`GrLivArea`) and basement area (`TotalBsmtSF`).
  * `TotalOutdoorArea`: Aggregates deck space (`WoodDeckSF`) and porch space (`OpenPorchSF`).
* **Robust Preprocessing Pipeline:** Uses a saved Scikit-Learn `OneHotEncoder` instance to dynamically align and transform categorical text inputs on incoming requests without runtime schema failures.
* **FastAPI Backend:** RESTful API featuring Pydantic type validation and automatic interactive documentation.
* **Streamlit Frontend:** An interactive, pure-Python web dashboard for seamless user input and real-time inference.
* **Containerized Deployment:** Both the frontend and backend are packaged into lightweight Docker images ready for isolated server hosting.

## 📁 Repository Structure

```text
.
├── main.py                       # FastAPI application logic & inference pipeline
├── Dockerfile                    # Docker build configuration for the backend
├── requirements.txt              # Production dependencies for the backend
├── rf_house_model.joblib         # Trained Random Forest Regressor artifact
├── house_encoder.joblib          # Fitted Scikit-Learn OneHotEncoder artifact
├── model_columns.joblib          # Expected column structure for feature alignment
├── house-price-prediction.ipynb  # Jupyter Notebook for EDA & model development
├── train.csv / test.csv          # Training and evaluation datasets
└── house-dashboard/              # Streamlit Frontend UI
    ├── app.py                    # Streamlit dashboard code
    ├── Dockerfile                # Docker build configuration for the frontend
    └── requirements.txt          # Frontend dependencies
```

## ⚙️ Local Installation & Setup

### Prerequisites
* Python 3.10+
* Git

### 1. Clone the Repository
```bash
git clone https://github.com/Abubakarr2603/House-price-predictor.git
cd House-price-predictor
```

### 2. Start the FastAPI Backend
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```
*The API runs at `http://localhost:8001`. Interactive docs at `http://localhost:8001/docs`.*

### 3. Start the Streamlit Dashboard (New Terminal)
```bash
cd house-dashboard
pip install -r requirements.txt
streamlit run app.py
```
*The UI will automatically open in your browser at `http://localhost:8501`.*

## 🐳 Docker Deployment

To build and run the complete application as isolated containers:

### 1. Backend Container
```bash
# In the root project directory:
docker build -t house-price-api .
docker run -d -p 8001:8000 --name house-price-backend --restart always house-price-api
```

### 2. Frontend Container
```bash
# In the house-dashboard directory:
cd house-dashboard
docker build -t house-price-ui .
docker run -d -p 8501:8501 --name house-price-frontend --restart always house-price-ui
```

## 📡 API Reference

### `POST /predict`
Accepts house attributes in JSON format and returns the estimated market value.

#### Sample Request:
```json
{
  "OverallQual": 7,
  "TotalIndoorArea": 2200.5,
  "YearBuilt": 2005,
  "LotArea": 8500.0,
  "GarageCars": 2,
  "TotalOutdoorArea": 250.0,
  "KitchenQual": "Gd",
  "BldgType": "1Fam"
}
```

#### Sample Response:
```json
{
  "predicted_price": 155273.44
}
```

## 📊 Model Summary

| Metric | Detail | 
| ----- | ----- | 
| **Model Type** | Random Forest Regressor | 
| **Evaluation Metric** | $R^2$ Score | 
| **Accuracy Score** | \~0.88 | 
| **Key Features** | `OverallQual`, `TotalIndoorArea`, `YearBuilt`, `LotArea` | 