import streamlit as st

# text input
name = st.text_input("Enter your name", "")
st.write("Your name is ", name)

age = st.number_input(label="Enter your age")
st.write("Your age is ", age)

address = st.text_area("Enter your address", "")
st.write("Your address is ", address)