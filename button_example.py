import streamlit as st
 
#button
if st.button('Click me', help="Click to see the text change"):
    st.write('Welcome to Streamlit!')
else:
    st.write('Hi there!')