import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from src.services.predict import predict_customer


st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="centered"
)

st.title("📉 Axiomeet")
st.caption(
    "Customer Churn Prediction Platform"
)

tenure = st.slider(
    "Tenure (months)",
    0,
    72,
    12
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=600.0
)

fiber = st.selectbox(
    "Fiber Internet",
    [0, 1]
)

contract = st.selectbox(
    "Two Year Contract",
    [0, 1]
)

if st.button("Predict"):

    result = predict_customer(
        {
            "tenure": tenure,

            "MonthlyCharges": monthly,

            "TotalCharges": total,

            "InternetService_Fiber optic": fiber,

            "Contract_Two year": contract
        }
    )

    if result["prediction"] == 1:

        st.error(
            "⚠️ High Churn Risk"
        )

    else:

        st.success(
            "✅ Customer Likely To Stay"
        )


    st.metric(
        "Churn Probability",
        f"{result['probability']*100:.1f}%"
    )

    st.divider()

st.caption(
    "Built by Axiomeet.com"
)