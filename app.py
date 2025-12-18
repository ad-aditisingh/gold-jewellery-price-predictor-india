import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_model():
    return joblib.load("linear_regression_jewellery_model.pkl")

model = load_model()

st.title("Gold Jewellery Price Estimator (India 🇮🇳)")

gold_rate = st.number_input("Gold Rate (₹/g)", min_value=1000.0)
weight = st.number_input("Weight (g)", min_value=0.1)
making_pct = st.number_input("Making (%)", min_value=0.0)
wastage_pct = st.number_input("Wastage (%)", min_value=0.0)

if st.button("Estimate Price"):
    X = np.array([[gold_rate, weight, making_pct, wastage_pct]])
    price = model.predict(X)[0]
    st.success(f"Estimated Price: ₹{price:,.2f}")
