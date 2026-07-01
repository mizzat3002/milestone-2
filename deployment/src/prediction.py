import pandas as pd
import streamlit as st
import joblib
import os
import sklearn

def run():
  path = os.path.join('src')
  model = joblib.load(os.path.join(path,'model_stroke.pkl'))
  df = pd.read_csv(os.path.join(path,'stroke_data.csv'))
  
  st.title('Stroke Prediction')
  st.markdown('Silahkan masukkan data medis pasien untuk memprediksi risiko stroke.')

  with st.form("my_form"):
    gender = st.selectbox('Gender', df.gender.unique())
    age = st.slider('Age', float(df.age.min()), float(df.age.max()))
    st.markdown('---')
    hypertension = st.selectbox('Hypertension', df.hypertension.unique())
    heart = st.selectbox('Heart Disease', df.heart_disease.unique())
    married = st.selectbox('Marriage Status', df.ever_married.unique())
    work = st.selectbox('Work Type', df.work_type.unique())
    residence = st.selectbox('Residence Type', df.Residence_type.unique())
    st.markdown('---')
    glucose = st.slider('Glucose Level', float(df.avg_glucose_level.min()), float(df.avg_glucose_level.max()))
    bmi = st.slider('Body Mass Index (BMI)', float(df.bmi.min()), float(df.bmi.max()))
    st.markdown('---')
    smoking = st.selectbox('Smoking Status', df.smoking_status.unique())
    submit = st.form_submit_button("Prediksi Risiko Stroke")

  if submit:
    data_pasien_baru = pd.DataFrame({
          'gender': [gender],
          'age': [age],
          'hypertension': [hypertension],       
          'heart_disease': [heart],      
          'ever_married': [married],
          'work_type': [work],
          'residence_type': [residence], 
          'avg_glucose_level': [glucose],
          'body_mass': [bmi],            
          'smoking_status': [smoking]
      })
    
    st.dataframe(data_pasien_baru)
    
    prediction = model.predict(data_pasien_baru)

    st.markdown('---')
    st.subheader('Hasil Analisis:')
    
    if prediction[0] == 1:
          st.error('Prediksi Akhir: Risiko Tinggi Terkena Stroke')
    else:
          st.success('Prediksi Akhir: Normal')



if __name__ =="__main__":
    run()