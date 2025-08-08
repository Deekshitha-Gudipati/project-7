import pickle
import numpy as np

with open("models/heart_model.pkl", "rb") as f:
    heart_model = pickle.load(f)

with open("models/diabetes_model.pkl", "rb") as f:
    diabetes_model = pickle.load(f)

def predict_heart_risk(data):
    input_data = np.array([list(data.values())])
    prediction = heart_model.predict(input_data)[0]
    return "High" if prediction == 1 else "Low"

def predict_diabetes_risk(data):
    input_data = np.array([list(data.values())])
    prediction = diabetes_model.predict(input_data)[0]
    return "High" if prediction == 1 else "Low"
