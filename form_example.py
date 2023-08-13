import streamlit as st

with st.form("user_form"):
   st.header("User Registration")
   name = st.text_input("Enter your name", "")
   age = st.slider("Enter your age")
   gender = st.radio("Select your gender", ('Male', 'Female'))
   terms = st.checkbox("Accept terms and conditions")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
        if terms:
            st.write("Name: ", name, ", Age: ", age, ", Gender: ", gender)
        else:
            st.write("Accept terms and conditions")

st.write("Thanks for visiting")