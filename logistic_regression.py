import pandas as pd 
import numpy as np 
import streamlit as st 

import pickle 

model=pickle.load(open('excelr_model.pkl','rb'))

st.title('Diabetes Predictor')


col1,col2=st.columns(2)
with col1:
    Pregnancies=st.number_input('No of Pregnanices')

with col2:
    Glucose=st.number_input('Glucose')


col3,col4,col5=st.columns(3)
with col3:
    BloodPressure=st.number_input('Blood Pressure')

with col4:
    SkinThickness=st.number_input('Skin Thickness')

with col5:
    Insulin=st.number_input('Insulin')

col6,col7=st.columns(2)
with col6:
    BMI=st.number_input('BMI')
    
with col7:
    DiabetesPedigreeFunction=st.number_input('Diabetes Pedigree Function')

Age=st.slider('Age',min_value=0,max_value=100)



if st.button('Predict'):
    data=np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    prediction=model.predict(data)
    

    if prediction == 1:
        st.error("⚠️ High chance of Diabetes")
    else:
        st.success("✅ Low chance of Diabetes")

