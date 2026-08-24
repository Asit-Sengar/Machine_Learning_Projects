# House Price Prediction

This project is a simple machine learning app that predicts house prices based on key property features such as area, bedrooms, bathrooms, stories, parking, and furnishing status. The app uses a regression model and a Streamlit interface so the prediction can be done quickly and easily from a browser.

## Overview

The goal of this project is to build a practical housing price predictor using real estate data. It includes data preprocessing, model training, evaluation, and a user-friendly web app for making predictions.

This project is useful for learning how machine learning can be applied to real-world prediction problems, especially in the field of property valuation.

## Tech Stack

- Python
- Streamlit
- pandas
- NumPy
- scikit-learn
- joblib
- Jupyter Notebook

## Project Structure

- [README.md](README.md) – project documentation
- [app.py](app.py) – Streamlit web app for entering input and getting predictions
- [House_Price_Prediction_Workflow.ipynb](House_Price_Prediction_Workflow.ipynb) – notebook with the training workflow and analysis
- [Housing.csv](Housing.csv) – dataset used to train the model
- [house_price_prediction_model.pkl](house_price_prediction_model.pkl) – saved trained model
- [requirements.txt](requirements.txt) – required Python packages
- [.gitignore](.gitignore) – local environment and generated file exclusions

## How It Works

1. The dataset is loaded from [Housing.csv](Housing.csv).
2. The data is explored and cleaned for model training.
3. A regression model is trained using property-related features.
4. The trained model is saved so it can be reused.
5. The user enters house details in the app, and the model predicts the estimated price.

## Run the Project Locally

### 1. Create a virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
streamlit run app.py
```

### 4. Open the notebook (optional)

```bash
jupyter notebook
```

## Model Input

The app expects values like:

- area
- number of bedrooms
- number of bathrooms
- number of stories
- parking availability
- furnishing status

## Notes

This project is a straightforward example of an end-to-end machine learning workflow. It shows how a trained model can be turned into an interactive tool that people can use without writing any code.

## Future Improvements

- try multiple regression algorithms to improve accuracy
- improve the visual design of the app
- add more detailed prediction explanations
- deploy the app online for public access

## Live Demo

https://house-price-prediction-asit.onrender.com
