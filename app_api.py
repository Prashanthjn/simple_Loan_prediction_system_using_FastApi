from signal import raise_signal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib 

app= FastAPI() 

try:
    model= joblib.load("loan_model.joblib")
except Exception:
    model=None

class LoanRequest(BaseModel):
    Age:int = Field(...,ge=18,le=60,description="age should be between 18 and 60")
    Salary: float =Field(...,gt=10000,description="salary should be greater than 10000")

@app.get("/")
def home():
    return {
        "message":"Loan Prediction API is Running"
    }

@app.get("/health")
def health():

    if model is None:
        return {
            "status":"Unhealthy",
            "model":"Not Loaded" 
        }
    return {
        "status":"Healthy",
        "model":"Loaded"
    }


@app.post("/predict")
def predict(data: LoanRequest):
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="model not found "
        )
    if data.Salary>1000000:
        raise HTTPException(
            status_code=400,
            detail="unrealistic salary input"
        )
    try:
        input_data = [[data.Age, data.Salary]]
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            result = "Loan Approved"
        else:
            result = "Loan Rejected"
        return {
            "prediction": result
        }
    except Exception:
        raise HTTPException(
            status_code=420,
            detail="unable to predict the loan approval"
        )