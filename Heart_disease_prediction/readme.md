# Heart Disease Prediction

A scikit-learn project that predicts heart disease from health and lifestyle data.

## Workflow

1. Load the data from `heart_disease_dataset.csv`.
2. Separate the input features from the `Heart Disease` target column.
3. Split the data into training and testing sets.
4. Fill missing values, scale numerical features, and one-hot encode categorical features.
5. Train a Logistic Regression model using the processed data.
6. Predict results for the test data.
7. Evaluate the model with accuracy, a confusion matrix, and a classification report.
8. Save the complete preprocessing and model pipeline as `disease_prediction.pkl`.

## Run the Project

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Open `disease_prediction.ipynb` and run the cells from top to bottom. The dataset is stored in `heart_disease_dataset.csv`, and the trained pipeline is saved as `disease_prediction.pkl`.

This project is for educational purposes only and is not a medical diagnostic tool.
