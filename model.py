import joblib
import pandas as pd
import streamlit as st

def tampilkan_model():
    st.title("Model Machine Learning")
    
    # Load the model
    model = joblib.load('ridge_model.joblib')
    
    # Input features
    st.header("Input Features")
    crim = st.number_input("Criminal Rate (crim)")
    zn = st.number_input("Residential Land Zone (zn)")
    indus = st.number_input("Non-retail Business Acres (indus)")
    chas = st.number_input("Is bounds with river (0/1)", step=1)
    nox = st.number_input("Nitric Oxide Concentration (nox)")
    rm = st.number_input("Number of Rooms (rm)")
    age = st.number_input("Older Homes Proportion (age)")
    dis = st.number_input("Weighted Distances to Employment Centers (dis)")
    tax = st.number_input("Property Tax Rate (tax)")
    ptratio = st.number_input("Pupil-Teacher Ratio (ptratio)")
    black = st.number_input("Black Population Proportion (black)")
    lstat = st.number_input("Lower Status of Population (lstat)")

    # Create a DataFrame for the input features
    input_data = pd.DataFrame([[
        crim, zn, indus, chas, nox, rm, age, dis, tax, ptratio, black, lstat
    ]], columns=[
        'crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age',
        'dis', 'tax', 'ptratio', 'black', 'lstat'
    ])
    
    # Make prediction
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.success(f"💰 Prediksi Harga Rumah: ${prediction[0]*1000:,.2f}")