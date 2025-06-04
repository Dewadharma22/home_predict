import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def tampilkan_visualisasi():
    st.title("Visualisasi Data Boston Housing")

    # Load the dataset
    df = pd.read_csv('boston.csv')

    # filter MEDV
    st.subheader("Filter Rentang Harga Rumah")
    st.write("Gunakan slider untuk memilih rentang harga rumah yang ingin ditampilkan.")
    harga_min = float(df['medv'].min())
    harga_max = float(df['medv'].max())

    harga_range = st.slider("Rentang Harga Rumah (000s USD)", 
                                    min_value=harga_min, max_value=harga_max, 
                                    value=(harga_min, harga_max), step=1.0)

    df_filtered = df[(df['medv'] >= harga_range[0]) & (df['medv'] <= harga_range[1])]


    # Distribution of the target variable (MEDV)
    st.subheader("Distribusi Harga Rumah (MEDV)")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df_filtered['medv'], bins=30, kde=True, ax=ax1)
    ax1.set_xlabel("Harga Rumah (ribu USD)")
    ax1.set_ylabel("Jumlah Rumah")
    st.pyplot(fig1)

    # Create a correlation heatmap
    st.subheader("Korelasi Fitur terhadap Harga Rumah")
    correlation = df_filtered.corr()['medv'].sort_values(ascending=False)
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(x=correlation.values, y=correlation.index, ax=ax2)
    st.pyplot(fig2)

    # Create a scater plot
    st.subheader("Hubungan Fitur terhadap Harga Rumah")
    fitur_pilihan = st.selectbox("Pilih fitur untuk scatter plot:", df.columns[:-1])
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=fitur_pilihan, y='medv', data=df_filtered, ax=ax3)
    ax3.set_xlabel(fitur_pilihan)
    ax3.set_ylabel("Harga Rumah (MEDV)")
    st.pyplot(fig3)

    # Display the filtered DataFrame
    with st.expander("Lihat Data yang Difilter"):
        st.dataframe(df_filtered)