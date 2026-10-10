# 🏡 House Price Predictor API

An end-to-end Machine Learning production service built with **Python**, **Scikit-Learn**, and **FastAPI**, containerized using **Docker** for continuous cloud deployment. 

This project takes raw real estate data from the Kaggle House Prices competition, cleans and engineers optimized features, trains a **Random Forest Regressor** model achieving an $R^2$ score of **~0.88**, and exposes a production-ready REST API for real-time property value predictions.

---

## 🚀 Project Highlights & Architecture

- **Machine Learning Model:** Random Forest Regressor trained on optimized house features.
- **Feature Engineering:** Combined redundant architectural inputs into intuitive super-features:
  - `TotalIndoorArea`: Aggregates above-ground living space (`GrLivArea`) and basement area (`TotalBsmtSF`).
  - `TotalOutdoorArea`: Aggregates deck space (`WoodDeckSF`) and porch space (`OpenPorchSF`).
- **Robust Preprocessing Pipeline:** Uses a saved Scikit-Learn `OneHotEncoder` instance to dynamically align and transform categorical text inputs on incoming requests without runtime schema failures.
- **FastAPI Backend:** RESTful API featuring Pydantic type validation and automatic interactive documentation (`/docs`).
- **Containerized Deployment:** Packaged into a lightweight Docker image ready for server hosting.

---

## 📁 Repository Structure

```text
.
├── main.py                       # FastAPI application logic & inference pipeline
├── Dockerfile                    # Docker build configuration for deployment
├── requirements.txt              # Production dependencies
├── rf_house_model.joblib         # Trained Random Forest Regressor artifact
├── house_encoder.joblib          # Fitted Scikit-Learn OneHotEncoder artifact
├── model_columns.joblib          # Expected column structure for feature alignment
├── house-price-prediction.ipynb  # Jupyter Notebook for EDA & model development
├── data_description.txt          # Original Kaggle field descriptions
├── train.csv                     # Training dataset
└── test.csv                      # Evaluation dataset
```

---

## ⚙️ Local Installation & Setup

### Prerequisites
- Python 3.10+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Abubakarr2603/House-price-predictor.git
cd House-price-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API Locally
```bash
uvicorn main:app --reload
```
The server will start at `http://127.0.0.1:8000`. You can interact with the API endpoints via Swagger UI at `http://127.0.0.1:8000/docs`.

---

## 🐳 Docker Deployment

To build and run the application as a isolated container:

### 1. Build the Docker Image
```bash
docker build -t house-price-api .
```

### 2. Run the Container
```bash
docker run -d -p 8000:8000 --name house-price-backend --restart always house-price-api
```
The service will run continuously in the background on port `8000`.

---

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

---

## 📊 Model Summary

| Metric | Detail |
| :--- | :--- |
| **Model Type** | Random Forest Regressor |
| **Evaluation Metric** | $R^2$ Score |
| **Accuracy Score** | ~0.88 |
| **Key Features** | `OverallQual`, `TotalIndoorArea`, `YearBuilt`, `LotArea` |