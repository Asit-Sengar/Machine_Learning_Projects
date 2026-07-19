import joblib  # for loading the model
import pandas as pd  # for making the datafram
import streamlit as st  # for creating website

model = joblib.load("house_price_prediction_model.pkl")
# it only loads the model

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Predict the selling price of a house using a trained Machine Learning model.")

st.header("Enter house details:")

area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=20000,
    value=3000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

stories = st.number_input(
    "Stories",
    min_value=1,
    max_value=5,
    value=2
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    max_value=5,
    value=1
)

mainroad = st.selectbox(
    "Main Road",
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)


furnishingstatus = st.selectbox(
    "Furnishing Status",
    [
        "furnished",
        "semi-furnished",
        "unfurnished"
    ]
)

user_input = pd.DataFrame({  # for creating dataframe of user data
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "mainroad": [mainroad],
    "guestroom": [guestroom],
    "basement": [basement],
    "hotwaterheating": [hotwaterheating],
    "airconditioning": [airconditioning],
    "parking": [parking],
    "prefarea": [prefarea],
    "furnishingstatus": [furnishingstatus]
})


# doing the final prediction and displaying it
if st.button("Predict Price"):
    prediction = model.predict(user_input)

    st.success(f"Estimated House Price: ₹{prediction[0]:,.0f}")
