import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load heart dataset
heart_df = pd.read_csv("data/heart.csv")
X_heart = heart_df.drop("target", axis=1)
y_heart = heart_df["target"]
heart_model = RandomForestClassifier().fit(X_heart, y_heart)

with open("models/heart_model.pkl", "wb") as f:
    pickle.dump(heart_model, f)

# Load diabetes dataset
diabetes_df = pd.read_csv("data/diabetes.csv")
X_diab = diabetes_df.drop("Outcome", axis=1)
y_diab = diabetes_df["Outcome"]
diabetes_model = RandomForestClassifier().fit(X_diab, y_diab)

with open("models/diabetes_model.pkl", "wb") as f:
    pickle.dump(diabetes_model, f)

print("✅ Models trained and saved.")
