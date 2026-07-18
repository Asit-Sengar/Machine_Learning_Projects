import streamlit as st  # for creating website
import pandas as pd  # for making the datafram
import joblib  # for loading the model

model = joblib.load("house_price_prediction_model.pkl")
# it only loads the model

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Predict the selling price of a house using a trained Machine Learning model.")
