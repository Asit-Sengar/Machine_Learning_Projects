import streamlit as st
import pandas as pd
import pickle

with open("disease_prediction.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Heart Disease Prediction")
