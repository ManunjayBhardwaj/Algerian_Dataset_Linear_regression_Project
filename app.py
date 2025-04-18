# app.py

import streamlit as st
import numpy as np
import pickle

# Load pre-trained model and scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('ElasticNetCV.pkl', 'rb'))


# Streamlit Page Setup
st.set_page_config(page_title="🔥 Algerian Forest Fire FWI Predictor", layout="centered")
st.title("🌲 Algerian Forest Fire Index Prediction App")
st.markdown("Enter environmental parameters to predict the **Fire Weather Index (FWI)**.")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("🌡️ Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
    rh = st.number_input("💧 Relative Humidity (%)", min_value=0, max_value=100, step=1)
    ws = st.number_input("🌬️ Wind Speed (km/h)", min_value=0, max_value=100, step=1)
    rain = st.number_input("🌧️ Rain (mm)", min_value=0.0, max_value=100.0, step=0.1)

with col2:
    ffmc = st.number_input("🔥 FFMC (Fine Fuel Moisture Code)", min_value=0.0, max_value=150.0, step=0.1)
    dmc = st.number_input("🔥 DMC (Duff Moisture Code)", min_value=0.0, max_value=300.0, step=0.1)
    isi = st.number_input("🔥 ISI (Initial Spread Index)", min_value=0.0, max_value=100.0, step=0.1)

classes = st.selectbox("🔥 Fire Class", options=["Fire", "Not Fire"])
class_encoded = 1 if classes == "Fire" else 0

# Prediction
if st.button("🔍 Predict FWI"):
    try:
        input_data = np.array([[temp, rh, ws, rain, ffmc, dmc, isi, class_encoded]])
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)
        st.success(f"🔥 Predicted Fire Weather Index (FWI): **{prediction[0]:.2f}**")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Manunjay Bhardwaj")
