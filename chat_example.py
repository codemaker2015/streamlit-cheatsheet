import streamlit as st
import numpy as np

prompt = st.chat_input("Enter the chart type (bar, area, line)")
print(prompt)
if prompt == "bar":
    with st.chat_message("user"):
        st.write("Bar Chart Demo 👋")
        st.bar_chart(np.random.randn(30, 3))
elif prompt == "area":
    with st.chat_message("user"):
        st.write("Area Chat Demo 👋")
        st.area_chart(np.random.randn(30, 3))
elif prompt == "line":
    with st.chat_message("user"):
        st.write("Line Chat Demo 👋")
        st.line_chart(np.random.randn(30, 3))
elif prompt is not None:
    with st.chat_message("user"):
        st.write("Wrong chart type")