# House Price Prediction

A machine learning project that predicts house prices using **Linear Regression**. The model learns from housing data and estimates prices based on features such as area, bedrooms, bathrooms, location, and other property details.

## Overview

The goal of this project is to build a simple and interpretable regression model for estimating house prices. It includes the main steps of a machine learning workflow: data preprocessing, exploratory analysis, model training, prediction, and evaluation.

## Tools Required

- Python
- Jupyter Notebook or VS Code
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Algorithm Used

**Linear Regression**

Linear Regression is used to predict a continuous value, in this case the price of a house. It finds the best relationship between the input features and the target price.

## Workflow

1. Load and inspect the dataset
2. Clean and preprocess the data
3. Explore feature relationships
4. Split data into training and testing sets
5. Train the Linear Regression model
6. Predict house prices
7. Evaluate model performance

## Evaluation Metrics

The model can be evaluated using:

- Mean Absolute Error
- Mean Squared Error
- Root Mean Squared Error
- R2 Score

## Project Structure

House_Price_Prediction/
├── README.md
├── data/
├── notebooks/
├── src/
└── requirements.txt

````

## How to Run

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
````

Run the notebook or Python script:

```bash
jupyter notebook
```

or

```bash
python src/model.py
```

## Future Scope

- Improve feature engineering
- Compare Linear Regression with other regression models
- Add model deployment using Streamlit or Flask
- Save predictions for later analysis

## Conclusion

This project demonstrates a practical approach to house price prediction using Linear Regression. It focuses on building a clear baseline model that is easy to understand, evaluate, and improve.
