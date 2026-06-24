import sys
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[2]
APP_DIR = Path(__file__).resolve().parent

sys.path.append(str(ROOT))
sys.path.append(str(APP_DIR))

import requests
import streamlit as st
from ui import show_result
from src.services.predict import predict_customer

ROOT = Path(__file__).resolve().parents[2]
APP_DIR = Path(__file__).resolve().parent

from ui import show_result

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api/v1/predict")

st.set_page_config(page_title="Axiomeet Analytics",layout="wide")

st.title("Axiomeet Customer Analytics")
st.caption("Customer churn prediction system using ML pipeline")

st.sidebar.header("Customer Input")

if "result" not in st.session_state:
    st.session_state.result = None

tenure = st.number_input("Tenure", 0, 72, 12)

monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)

total = st.number_input("Total Charges", 0.0, 10000.0, 600.0)

fiber = st.checkbox("Fiber Optic")

contract = st.checkbox("Two Year Contract")

if st.button("Predict"):

    payload = {
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "InternetService_Fiber_optic": int(fiber),
        "Contract_Two_year": int(contract)
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=3)
        response.raise_for_status()
        st.session_state.result = response.json()

    except Exception:
        st.warning("API unavailable → using local model")
        st.session_state.result = predict_customer(payload)

if st.session_state.result is not None:

    result = st.session_state.result

    st.divider()

    st.subheader("Prediction Result")

    show_result(result)

    st.divider()

    st.subheader("Why this prediction?")

    for feature, impact in result["explanation"]:
        if impact > 0:
            st.write(f"🔴 increases churn risk: **{feature}** ({impact:.3f})")
        else:
            st.write(f"🟢 reduces churn risk: **{feature}** ({impact:.3f})")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### About Me")
    st.write("Pourya Einolghazaei")
    st.write("ML Engineer | Data Science | MLSecOps Enthusiast")

with col2:
    st.markdown("### Project Info")

    st.write("Customer churn prediction system using ML pipeline")

st.markdown("---")

st.caption("📧 axiomeet@gmail.com | 🌐 axiomeet.com")

st.caption("© 2026 Axiomeet - Personal Project")