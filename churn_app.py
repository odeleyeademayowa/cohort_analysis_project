import streamlit as st
import pandas as pd
import joblib  # To load the model
import numpy as np

# Load the trained model
model = joblib.load(r'C:\Users\lapt\Desktop\cohort_analysis_project\notebooks\best_random_forest_model.pkl')
st.title("📊 Customer Churn Prediction")
st.write("Adjust the features below to see the churn prediction:")

# Add sliders for user input
recency = st.slider('Recency (days since last purchase)', 0, 365, 30)
frequency = st.slider('Frequency (number of purchases)', 0, 100, 5)
monetary = st.slider('Monetary (total amount spent)', 0, 1000000, 10000)
pred_purchases = st.slider('Predicted Purchases (90d)', 0, 50, 5)
pred_monetary = st.slider('Predicted Monetary (90d)', 0, 1000000, 10000)
pred_clv = st.slider('Predicted CLV (90d)', 0, 1000000, 10000)

# Make prediction when button is clicked
if st.button('Predict Churn'):
    # Prepare the input data for prediction
    input_data = [[recency, frequency, monetary, pred_purchases, pred_monetary, pred_clv]]
    
    # Make prediction
    prediction = model.predict(input_data)
    
    if prediction == 0:
        st.write("🎉 The customer is likely to stay!")
    else:
        st.write("⚠️ The customer is likely to churn.")