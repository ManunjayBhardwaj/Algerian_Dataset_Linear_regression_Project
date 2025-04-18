# 🔥 Algerian Forest Fire FWI Prediction App

This project predicts the **Fire Weather Index (FWI)** using meteorological and fire-related data from the **Algerian Forest Fires Dataset**. The app is built using **Streamlit** and deployed on **Streamlit Cloud**.

---

## 🚀 Live Demo

👉 https://algeriandatasetlinearregressionproject-kfujjbmgv6aha5ynehdrfu.streamlit.app
> Replace this link with your actual Streamlit Cloud deployment link after deploying the app.

---

## 📊 Project Overview

Wildfires can have a devastating impact on the environment and human life. This app uses machine learning to predict the **Fire Weather Index (FWI)**, which indicates the potential risk of a forest fire. The prediction is based on various weather and environmental features from real-world Algerian forest fire data.

---

## 🧠 Machine Learning Pipeline

- **Dataset**: Algerian Forest Fires Dataset (UCI ML Repository)
- **Features Used**:
  - Temperature
  - Relative Humidity (RH)
  - Wind Speed (Ws)
  - Rain
  - FFMC, DMC, ISI
  - Class (Fire / Not Fire)
- **Target Variable**: Fire Weather Index (FWI)
- **Final Model**: `ElasticNetCV` with cross-validation
- **Preprocessing**: StandardScaler

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn
- Pickle (for model serialization)

---

## 📁 Project Structure

