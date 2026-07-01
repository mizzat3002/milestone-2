import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from PIL import Image


def run():
    st.title("Stroke Prediction")
    path = os.path.join('src','stroke_data.csv')
    image = Image.open(os.path.join('src','images-3.jpeg'))
    st.image(image)

    st.header("Data Analysis")
    
    df = pd.read_csv(path)
    st.dataframe(df)

    # cek distribusi data
    st.subheader('Distribusi Data')
    st.caption('grafik ini menjelaskan bahwa jumlah pasien sehat(0) lebih mendominasi jauh ketimbang jumlah pasien yang terkena stroke(1), dapat diketahui juga dari rata2 statistik pada kolom stroke bernilai 0,048 atau 4,8%. ini menunjukkan bahwa dataset yang kita gunakan mengalami ketidak seimbangan distribusi data ')
    distribusi = plt.figure(figsize=(8,5))
    sns.countplot(x='stroke', data=df, palette='Set2')
    plt.title('Distribusi Pasien Stroke vs Sehat')
    plt.xlabel('Status Stroke (0 = Sehat, 1 = Stroke)')
    plt.ylabel('Jumlah Pasien')
    plt.show()

    st.pyplot(distribusi)

    # membuat plot histogram untuk kelompok umur 
    st.subheader('Distribusi Jumlah Pasien per Kelompok Umur')
    st.caption('dari plot dibawah ini menunjukkan kalau semakin naik umur seseorang semakin punya resiko terkena stroke, resiko stroke itu meningkat secara non-linear pada rentang umur 40-80 tahun, artinya di rentang inilah seseorang itu beresiko terkena stroke secara drastis')
    fig_umur, ax_umur = plt.subplots(figsize=(8, 5))
    sns.histplot(ax=ax_umur, data=df, x='age', hue='stroke', multiple='stack', palette='Set1', bins=20)
    ax_umur.set_title('Distribusi Jumlah Pasien per Kelompok Umur')
    ax_umur.set_xlabel('Umur Pasien (Tahun)')
    ax_umur.set_ylabel('Jumlah Pasien')
 
    # Masukkan objek fig_umur ke st.pyplot
    st.pyplot(fig_umur)

    # membuat plot histogram untuk kelompok umur 
    st.subheader('Distribusi Jumlah Pasien per Kelompok Body Mass Index (BMI)')
    st.caption('pasien yang mengalami stroke terlihat menumpuk pada rentang nilai BMI 25-35, artinya di rentang inilah seseorang bisa terkena resiko stroke meningkat drastis')
    fig_bmi, ax_bmi = plt.subplots(figsize=(8, 5))
    sns.histplot(ax=ax_bmi, data=df, x='bmi', hue='stroke', multiple='stack', palette='Set1', bins=20)
    ax_bmi.set_title('Distribusi Jumlah Pasien per Kelompok Body Mass Index (BMI)')
    ax_bmi.set_xlabel('Body Mass Index')
    ax_bmi.set_ylabel('Jumlah Pasien')

    st.pyplot(fig_bmi)

    # melihat distribusi status merokok terhadap stroke
    st.subheader('Rata-rata Stroke berdasarkan Status Merokok')
    st.caption('pasien dengan status mrokoknya adalah mantan perokok mempunyai nilai tertingggi diantara status yang lain')
    smoke = plt.figure(figsize=(7,4))
    sns.barplot(data=df, x="smoking_status", y="stroke")
    plt.title("Rata-rata Stroke berdasarkan Status Merokok")
    plt.xlabel("Status Merokok")
    plt.show()

    st.pyplot(smoke)
 
   





if __name__=="__main__":
    run()