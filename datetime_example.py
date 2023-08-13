import datetime
import streamlit as st

date = st.date_input("When's your birthday", datetime.date(2000, 1, 1), datetime.date(1990, 1, 1), datetime.datetime.now())
st.write("Your birthday is ", date)

time = st.time_input("Which is your birth time", datetime.time(0, 0))
st.write("Your birth time is ", time)