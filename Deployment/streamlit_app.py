
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Water Potability Prediction",
    page_icon="💧",
    layout="wide"
)

# Load trained ML model
BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "Model" / "water_potability_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# Application heading
st.title("💧 Water Potability Prediction")
st.write(
    "Enter the water quality parameters below to predict "
    "whether the water sample is classified as potable."
)

st.divider()

# Input form
st.subheader("Enter Water Quality Parameters")

with st.form("water_quality_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        ph = st.number_input("pH", value=7.0)
        hardness = st.number_input("Hardness", value=200.0)
        solids = st.number_input("Solids", value=15000.0)

    with col2:
        chloramines = st.number_input("Chloramines", value=7.0)
        sulfate = st.number_input("Sulfate", value=300.0)
        conductivity = st.number_input("Conductivity", value=400.0)

    with col3:
        organic_carbon = st.number_input("Organic Carbon", value=10.0)
        trihalomethanes = st.number_input("Trihalomethanes", value=70.0)
        turbidity = st.number_input("Turbidity", value=4.0)

    submit = st.form_submit_button("Predict Water Potability")

# Prediction
if submit:

    input_data = pd.DataFrame([{
        "ph": ph,
        "Hardness": hardness,
        "Solids": solids,
        "Chloramines": chloramines,
        "Sulfate": sulfate,
        "Conductivity": conductivity,
        "Organic_carbon": organic_carbon,
        "Trihalomethanes": trihalomethanes,
        "Turbidity": turbidity
    }])

    prediction = model.predict(input_data)[0]

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("Prediction: Potable")
        st.write("The model classifies this sample as potable.")
    else:
        st.error("Prediction: Not Potable")
        st.write("The model classifies this sample as not potable.")

    st.caption(
        "Educational ML prediction only. This model is not a "
        "certified test of drinking-water safety."
    )

