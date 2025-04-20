from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("model/isolation_forest.pkl")

app = FastAPI(title="Credit Card Fraud Detection API")

# Define input format (based on Kaggle dataset excluding 'Time' and 'Class')
class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float
@app.get("/")
def root():
    return {"message": "Welcome to creadit card fraud detection"}

@app.post("/predict")
def predict(transaction: Transaction):
    data = np.array([list(transaction.dict().values())])
    prediction = model.predict(data)
    result = "Fraudulent" if prediction[0] == -1 else "Normal"
    return {"prediction": result}

