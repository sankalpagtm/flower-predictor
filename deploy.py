import streamlit as st
import joblib
import numpy as np

# loads saved model
model = joblib.load('model.joblib')

st.title("🌿 Flower Predictor")
st.write("Enter the measurements to identify the flower species.")

# input fields for the 4 features
sepal_l = st.number_input("Sepal Length", value=5.0)
sepal_w = st.number_input("Sepal Width", value=3.0)
petal_l = st.number_input("Petal Length", value=4.0)
petal_w = st.number_input("Petal Width", value=1.0)

if st.button("Predict"):
    # input into 2D
    features = np.array([[sepal_l, sepal_w, petal_l, petal_w]])
    
    # prediction 
    prediction = model.predict(features)
    
    # result
    st.success(f"The predicted species is: *{prediction[0]}*")

