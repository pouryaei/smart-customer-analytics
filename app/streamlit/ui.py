import streamlit as st


def show_result(result):
    if result["prediction"] == 1:
        st.error("⚠️ High Churn Risk")
    else:
        st.success("✅ Customer Likely To Stay")

    st.progress(float(result["probability"]))
    st.metric(
        "Churn Probability",
        f"{result['probability'] * 100:.1f}%"
    )