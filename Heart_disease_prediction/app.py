import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

MODEL_PATH = Path(__file__).resolve().parent / "disease_prediction.pkl"

with MODEL_PATH.open("rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Heart Disease Prediction",
    layout="centered",
)

st.title("Heart Disease Prediction")
st.write("Enter the patient's information to get a prediction.")

st.header("Patient details")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=50)
        cholesterol = st.number_input(
            "Cholesterol", min_value=50, max_value=500, value=200)
        blood_pressure = st.number_input(
            "Blood Pressure", min_value=50, max_value=220, value=120)
        heart_rate = st.number_input(
            "Heart Rate", min_value=30, max_value=200, value=72)
        exercise_hours = st.number_input(
            "Exercise Hours", min_value=0, max_value=20, value=3)
        stress_level = st.number_input(
            "Stress Level", min_value=0, max_value=10, value=5)
        blood_sugar = st.number_input(
            "Blood Sugar", min_value=40, max_value=250, value=110)

    with col2:
        gender = st.selectbox("Gender", ["Female", "Male"])
        smoking = st.selectbox("Smoking", ["Current", "Former", "Never"])
        alcohol_intake = st.selectbox("Alcohol Intake", ["Heavy", "Moderate"])
        family_history = st.selectbox("Family History", ["No", "Yes"])
        diabetes = st.selectbox("Diabetes", ["No", "Yes"])
        obesity = st.selectbox("Obesity", ["No", "Yes"])
        exercise_induced_angina = st.selectbox(
            "Exercise Induced Angina", ["No", "Yes"])
        chest_pain_type = st.selectbox(
            "Chest Pain Type",
            ["Asymptomatic", "Atypical Angina",
                "Non-anginal Pain", "Typical Angina"],
        )

    predict_button = st.form_submit_button("Predict")

if predict_button:
    user_input = pd.DataFrame(
        [{
            "Age": age,
            "Gender": gender,
            "Cholesterol": cholesterol,
            "Blood Pressure": blood_pressure,
            "Heart Rate": heart_rate,
            "Smoking": smoking,
            "Alcohol Intake": alcohol_intake,
            "Exercise Hours": exercise_hours,
            "Family History": family_history,
            "Diabetes": diabetes,
            "Obesity": obesity,
            "Stress Level": stress_level,
            "Blood Sugar": blood_sugar,
            "Exercise Induced Angina": exercise_induced_angina,
            "Chest Pain Type": chest_pain_type,
        }],
        columns=model.feature_names_in_,
    )

    prediction = model.predict(user_input)[0]
    probability = model.predict_proba(user_input)[0][1]
    risk_label = "High risk" if prediction == 1 else "Low risk"

    if prediction == 1:
        st.error(f"Prediction: {risk_label} ({probability:.2%})")
        st.warning(
            "The model found signs associated with heart disease. Please speak with a medical professional.")
    else:
        st.success(f"Prediction: {risk_label} ({probability:.2%})")
        st.info("The model did not find strong signs of heart disease.")
