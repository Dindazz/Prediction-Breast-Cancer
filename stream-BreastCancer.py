import pickle
import streamlit as st

breast_model = pickle.load(open('breast_model.sav', 'rb'))

st.title('Prediction Breast Cancer')

col1, col2 = st.columns(2)
with col1 :
    id = st.number_input ('Input Nilai id')
with col2 :
    clump_thickness = st.number_input ('Input Nilai clump thickness')
with col1 :
    size_uniformity = st.number_input ('Input Nilai size uniformity')
with col2 :
    shape_uniformity = st.number_input ('Input Nilai shape uniformity')
with col1 :
    marginal_adhesion = st.number_input ('Input Nilai marginal adhesion')
with col2 :
    epithelial_size = st.number_input ('Input Nilai epithelial size')
with col1 :
    bare_nucleoli = st.number_input ('Input Nilai bare nucleoli')
with col2 :
    bland_chromatin = st.number_input ('Input Nilai bland chromatin')
with col1 :
    normal_nucleoli = st.number_input ('Input Nilai normal_nucleoli')
with col2 :
    mitoses = st.number_input ('Input Nilai mitoses')

breast_diagnosis = ''

if st.button('Test Prediction') :
    breast_prediction = breast_model.predict([[id, clump_thickness, size_uniformity, shape_uniformity, marginal_adhesion, epithelial_size, bare_nucleoli, bland_chromatin, normal_nucleoli, mitoses]])

    if (breast_prediction[0] == 2):
        breast_diagnosis = 'Kanker Jinak'
    if (breast_prediction[0] == 4):
        breast_diagnosis = 'Kanker Ganas'

st.success(breast_diagnosis)