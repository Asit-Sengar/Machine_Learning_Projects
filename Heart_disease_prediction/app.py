from pathlib import Path
import pickle

# this is for opening the trained model with the file
with open("disease_prediction.pkl", "rb") as file:
    model = pickle.load(file)  # now we will use the name model


import pandas as pd
import streamlit as st

st.set_page_config(  # this is for setting the page configuration
    page_title="Heart Disease Prediction",
    page_icon="💀"
)

st.title("Heart Disease Prediction")
st.write("Please enter patient's information")

age = st.number_input(
    "Age",  # this is the exact column name of the dataframe which the model is trained upon
    min_value=1,
    max_value=100
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=150,
    max_value=349
)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=90,
    max_value=179
)

heart_rate = st.number_input(
    "Heart Rate",
    min_value=60,
    max_value=99
)

smoking = st.selectbox(
    "Smoking",
    ["Current", "Former", "Never"]
)

alcohol_intake = st.selectbox(
    "Alcohol Intake",
    ["Heavy", "Moderate", "None"]
)

exercise_hours = st.number_input(
    "Exercise Hours",
    min_value=0,
    max_value=9
)

family_history = st.selectbox(
    "Family History",
    ["No", "Yes"]
)

diabetes = st.selectbox(
    "Diabetes",
    ["No", "Yes"]
)

obesity = st.selectbox(
    "Obesity",
    ["No", "Yes"]
)

stress_level = st.number_input(
    "Stress Level",
    min_value=1,
    max_value=10
)

blood_sugar = st.number_input(
    "Blood Sugar",
    min_value=70,
    max_value=199
)

exercise_induced_angina = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)

chest_pain_type = st.selectbox(
    "Chest Pain Type",
    ["Asymptomatic", "Atypical Angina", "Non-anginal Pain", "Typical Angina"]
)


# now i want to create a dataframe of the entered value
input_dataframe = pd.DataFrame({
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
})


# predicting the final outcome
final_prediction = model.predict(input_dataframe)
if (final_prediction[0] == 1):
    st.warning("you have high chances of heart disease")
else:
    st.success("you are at low risk")
