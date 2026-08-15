import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("customer_churn_model.pkl")

st.set_page_config(page_title="Bank Customer Churn Prediction")

st.title("🏦 Bank Customer Churn Prediction")

st.write("Enter customer details below to predict churn probability.")

# Inputs

credit_score = st.number_input(
    "Credit Score",
    min_value=0,
    max_value=850,
    value=650
)

country = st.selectbox(
    "Country",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=92,
    value=35
)

tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Balance",
    min_value=0.0,
    max_value=238387.56,
    value=50000.0
)

products_number = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=4,
    value=1
)

credit_card = st.selectbox(
    "Has Credit Card",
    [0, 1]
)

active_member = st.selectbox(
    "Is Active Member",
    [0, 1]
)

estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=11.58,
    max_value=199992.48,
    value=50000.0
)

# Prediction

if st.button("Predict Churn"):

    input_data = pd.DataFrame({
        "credit_score": [credit_score],
        "country": [country],
        "gender": [gender],
        "age": [age],
        "tenure": [tenure],
        "balance": [balance],
        "products_number": [products_number],
        "credit_card": [credit_card],
        "active_member": [active_member],
        "estimated_salary": [estimated_salary]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )