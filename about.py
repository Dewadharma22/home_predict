import streamlit as st

def tampilkan_tentang_saya():
    st.title("About This Application")
    st.write("""
    Welcome to the **Boston Housing Price Prediction App**.  
    This web application is built using **Streamlit** and allows users to:

    - Predict house prices using a trained **Ridge Regression** model
    - Visualize the distribution, correlation, and relationship between features
    - Interact with real housing data from the **Boston Housing Dataset**

    ---
    ### Features:
    - **Machine Learning Model**: Predict house prices based on various features using a Ridge Regression model.
    - **Data Visualization**: Explore the dataset with interactive visualizations, including histograms, scatter plots, and correlation heatmaps.
    - **User-Friendly Interface**: Easy-to-use interface with sliders and input fields for model predictions.
    - **Data Filtering**: Filter the dataset based on house prices to focus on specific ranges.
    ### Technologies Used:
    - **Streamlit**: For building the web application.
    - **Pandas**: For data manipulation and analysis.
    - **Seaborn** and **Matplotlib**: For data visualization.
    - **Scikit-learn**: For machine learning model training and prediction.
    ### Dataset:
    - The application uses the **Boston Housing Dataset**, which contains information about housing in Boston, including features like crime rate, number of rooms, and property tax rate.
    """)