import streamlit as st
 
# check box
checked = st.checkbox('Click me')
if checked:
    st.write('You agreed the terms and conditions!')