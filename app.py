import streamlit as st
import joblib
import numpy as np
import os

# Load trained model
MODEL_PATH = "linear_regression_jewellery_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("Model file not found. Please add linear_regression_jewellery_model.pkl")
else:
    model = joblib.load(MODEL_PATH)

    st.title("Gold Jewellery Price Estimator (India 🇮🇳)")
    st.write("Enter jewellery details to estimate price")

    gold_rate = st.number_input(
        "Gold Rate (₹ per gram, 22K)",
        min_value=1000.0,
        step=10.0
    )

    weight = st.number_input(
        "Weight (grams)",
        min_value=0.1,
        step=0.1
    )

    making_charge = st.number_input(
        "Making Charges (%)",
        min_value=0.0,
        step=0.5
    )

    if st.button("Estimate Price"):
        features = np.array([[gold_rate, weight, making_charge]])
        prediction = model.predict(features)[0]

        st.success(f"Estimated Jewellery Price: ₹{prediction:,.2f}")
