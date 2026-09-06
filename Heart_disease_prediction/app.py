from pathlib import Path
import pickle

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon=":heart:",
    layout="centered",
)

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "disease_prediction.pkl"


def repair_model_compatibility(model):
    preprocessor = model.named_steps.get("preprocessed_data")
    if preprocessor is None:
        return model

    for transformer in preprocessor.named_transformers_.values():
        imputer = getattr(transformer, "named_steps", {}).get("imputer")
        if (
            imputer is not None
            and not hasattr(imputer, "_fill_dtype")
            and hasattr(imputer, "_fit_dtype")
        ):
            imputer._fill_dtype = imputer._fit_dtype

    return model


@st.cache_resource
def load_model():
    with MODEL_PATH.open("rb") as file:
        model = pickle.load(file)

    return repair_model_compatibility(model)


model = load_model()

st.title("Heart Disease Prediction")
st.write("Enter patient health details to estimate the chance of heart disease.")

with st.form("prediction_form"):
    st.subheader("Patient Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=45)
        gender = st.selectbox("Gender", ["Female", "Male"])
        cholesterol = st.number_input(
            "Cholesterol",
            min_value=100,
            max_value=500,
            value=220,
        )
        blood_pressure = st.number_input(
            "Blood Pressure",
            min_value=70,
            max_value=220,
            value=120,
        )
        heart_rate = st.number_input(
            "Heart Rate",
            min_value=40,
            max_value=180,
            value=75,
        )
        blood_sugar = st.number_input(
            "Blood Sugar",
            min_value=50,
            max_value=300,
            value=100,
        )
        exercise_hours = st.number_input(
            "Exercise Hours",
            min_value=0,
            max_value=20,
            value=3,
        )

    with col2:
        smoking = st.selectbox("Smoking", ["Never", "Former", "Current"])
        alcohol_intake = st.selectbox(
            "Alcohol Intake", ["None", "Moderate", "Heavy"])
        family_history = st.selectbox("Family History", ["No", "Yes"])
        diabetes = st.selectbox("Diabetes", ["No", "Yes"])
        obesity = st.selectbox("Obesity", ["No", "Yes"])
        stress_level = st.slider(
            "Stress Level", min_value=1, max_value=10, value=5)
        exercise_induced_angina = st.selectbox(
            "Exercise Induced Angina",
            ["No", "Yes"],
        )
        chest_pain_type = st.selectbox(
            "Chest Pain Type",
            [
                "Typical Angina",
                "Atypical Angina",
                "Non-anginal Pain",
                "Asymptomatic",
            ],
        )

    submitted = st.form_submit_button("Predict")

if submitted:
    user_input = pd.DataFrame(
        {
            "Age": [age],
            "Gender": [gender],
            "Cholesterol": [cholesterol],
            "Blood Pressure": [blood_pressure],
            "Heart Rate": [heart_rate],
            "Smoking": [smoking],
            "Alcohol Intake": [alcohol_intake],
            "Exercise Hours": [exercise_hours],
            "Family History": [family_history],
            "Diabetes": [diabetes],
            "Obesity": [obesity],
            "Stress Level": [stress_level],
            "Blood Sugar": [blood_sugar],
            "Exercise Induced Angina": [exercise_induced_angina],
            "Chest Pain Type": [chest_pain_type],
        }
    )

    prediction = model.predict(user_input)[0]

    if prediction == 1:
        st.error("Prediction: Heart disease risk detected.")
    else:
        st.success("Prediction: No heart disease risk detected.")

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(user_input)[0][1] * 100
        st.metric("Estimated Risk Probability", f"{probability:.2f}%")
