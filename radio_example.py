import streamlit as st
 
# radio button
lang = st.radio(
    "What's your favorite programming language?",
    ('C','C++', 'Java','Python'))
 
if lang == 'C':
    st.write('You selected C')
elif lang == 'C++':
    st.write('You selected C++')
elif lang == 'C++':
    st.write('You selected Java')
else: 
    st.write('You selected Python')