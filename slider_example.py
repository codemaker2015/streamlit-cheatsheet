import streamlit as st
 
# slider
age = st.slider('Please enter your age', 
                   min_value=0, max_value=100, value=10)
st.write("Your age is ", age)