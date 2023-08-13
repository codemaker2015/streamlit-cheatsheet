import streamlit as st
import time

# progress
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

# spinner
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

# messages 
st.toast('Your edited image was saved!', icon='😍')
st.error('This is an error', icon="🚨")
st.info('This is a purely informational message', icon="ℹ️")
st.warning('This is a warning', icon="⚠️")
st.success('This is a success message!', icon="✅")
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)