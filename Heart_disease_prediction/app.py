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

cholestrol = st.number_input(
    "Cholesterol",
    min_value=150,
    max_value=349
)
