
# Water Potability Prediction Using Machine Learning

## Project Overview

This project implements an end-to-end machine learning
pipeline to predict water potability based on nine
water quality parameters.

## Problem Statement

To develop a machine learning model that classifies
water samples as potable or not potable based on
their physicochemical properties.

## Dataset

- Dataset: Water Potability Dataset
- Total Records: 3276
- Input Features: 9
- Target Variable: Potability
- 0: Not Potable
- 1: Potable

## Input Features

1. pH
2. Hardness
3. Solids
4. Chloramines
5. Sulfate
6. Conductivity
7. Organic Carbon
8. Trihalomethanes
9. Turbidity

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- FastAPI
- Streamlit
- GitHub

## Machine Learning Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

## Project Methodology

1. Dataset Collection
2. Exploratory Data Analysis
3. Data Preprocessing
4. Feature Scaling
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Hyperparameter Tuning using GridSearchCV
9. Best Model Selection
10. Model Serialization using Joblib
11. REST API Development using FastAPI
12. Web Application Development using Streamlit
13. Cloud Deployment

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Project Structure

    Water-Potability-Prediction/
    ├── Dataset/
    │   └── water_potability.csv
    ├── Model/
    │   └── water_potability_model.pkl
    ├── Deployment/
    │   ├── app.py
    │   ├── streamlit_app.py
    │   └── requirements.txt
    ├── Notebooks/
    │   └── Water_Potability_Project.ipynb
    └── README.md

## REST API

The trained machine learning model is integrated
with FastAPI and tested using Swagger UI.

API Endpoints:

- GET / : API status
- POST /predict : Water potability prediction

## Live Web Application

The Streamlit application allows users to enter
nine water quality parameters and obtain a prediction.

[Open Live Application](https://water-quality-predictor-aryan.streamlit.app/)

## Conclusion

This project demonstrates the complete machine
learning lifecycle, including data preprocessing,
model training, evaluation, optimization, REST API
development and cloud-based web application deployment.

## Disclaimer

This application is developed for educational purposes.
Its predictions should not be used as a substitute
for certified laboratory water safety testing.
