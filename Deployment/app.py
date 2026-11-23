
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load the trained model
model = joblib.load("Model/water_potability_model.pkl")

# Create FastAPI application
app = FastAPI(
    title="Water Potability Prediction API",
    description="API for predicting water potability using Machine Learning",
    version="1.0"
)

# Define input features
class WaterQuality(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

# Home endpoint
@app.get("/")
def home():
    return {"message": "Water Potability Prediction API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: WaterQuality):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = int(model.predict(input_data)[0])

    result = (
        "Potable"
        if prediction == 1
        else "Not Potable"
    )

    return {
        "prediction": prediction,
        "result": result
    }
