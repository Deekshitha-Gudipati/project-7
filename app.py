import streamlit as st
import pandas as pd
from ml_model import predict_heart_risk, predict_diabetes_risk
from recommendation_engine import get_recommendations

st.set_page_config(page_title="AI Health Analytics", layout="centered")

st.title("🧠 AI-Powered Health Analytics Platform")

# Tabs for Heart and Diabetes
tabs = st.tabs(["❤️ Heart Risk", "🩸 Diabetes Risk"])

with tabs[0]:
    st.header("Heart Disease Prediction")

    age = st.slider("Age", 18, 100, 50)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol Level", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality"])
    thalach = st.number_input("Max Heart Rate Achieved", 70, 210, 150)
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)

    if st.button("Predict Heart Disease Risk"):
        input_data = {
            "age": age,
            "sex": 1 if sex == "Male" else 0,
            "cp": ["Typical Angina", "Atypical Angina", "Non-anginal", "Asymptomatic"].index(cp),
            "trestbps": trestbps,
            "chol": chol,
            "fbs": 1 if fbs == "Yes" else 0,
            "restecg": 0 if restecg == "Normal" else 1,
            "thalach": thalach,
            "exang": 1 if exang == "Yes" else 0,
            "oldpeak": oldpeak
        }
        risk = predict_heart_risk(input_data)
        rec = get_recommendations("heart", risk)
        st.success(f"Predicted Risk: {risk}")
        st.info(rec)

with tabs[1]:
    st.header("Diabetes Prediction")

    preg = st.slider("Pregnancies", 0, 15, 1)
    glucose = st.slider("Glucose Level", 50, 200, 100)
    bp = st.slider("Blood Pressure", 30, 130, 70)
    skin = st.slider("Skin Thickness", 0, 100, 20)
    insulin = st.slider("Insulin", 0, 900, 80)
    bmi = st.slider("BMI", 10.0, 60.0, 25.0)
    dpf = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
    age_d = st.slider("Age", 10, 100, 33)

    if st.button("Predict Diabetes Risk"):
        input_data = {
            "Pregnancies": preg,
            "Glucose": glucose,
            "BloodPressure": bp,
            "SkinThickness": skin,
            "Insulin": insulin,
            "BMI": bmi,
            "DiabetesPedigreeFunction": dpf,
            "Age": age_d
        }
        risk = predict_diabetes_risk(input_data)
        rec = get_recommendations("diabetes", risk)
        st.success(f"Predicted Risk: {risk}")
        st.info(rec)
