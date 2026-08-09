import streamlit as st
import pandas as pd
import joblib

model = joblib.load("abdelrhman mohammed fouad Day 10 Task 3.pkl")

st.title("Diabetes Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 1, 100)
hypertension = st.selectbox("Hypertension", [0,1])
heart_disease = st.selectbox("Heart Disease", [0,1])
smoking_history = st.selectbox(
    "Smoking History",
    ["never","former","current","not current","ever","No Info"]
)
bmi = st.number_input("BMI")
HbA1c_level = st.number_input("HbA1c Level")
blood_glucose_level = st.number_input("Blood Glucose Level")

if st.button("Predict"):

    sample = pd.DataFrame({
        "gender":[gender],
        "age":[age],
        "hypertension":[hypertension],
        "heart_disease":[heart_disease],
        "smoking_history":[smoking_history],
        "bmi":[bmi],
        "HbA1c_level":[HbA1c_level],
        "blood_glucose_level":[blood_glucose_level]
    })

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error("Diabetes Detected")
    else:
        st.success("No Diabetes")