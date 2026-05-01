import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🩺 Diabetes Prediction System")

preg = st.number_input("Pregnancies")
glu = st.number_input("Glucose")
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness")
ins = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):
    data = np.array([[preg, glu, bp, skin, ins, bmi, dpf, age]])
    result = model.predict(data)

    if result[0] == 1:
        st.error("Diabetes Positive ⚠️")
    else:
        st.success("Diabetes Negative ✅")