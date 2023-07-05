import streamlit as st
from text_to_speech import read_text , stop_speech

st.title('WRITE WITH VOICE')
st.header('by Raviteja')

st.caption('THE SPEED DENOTES WORDS PER MINUTE')
st.caption('RECOMMENDED SPEED 120-180')

user_input = st.text_area('Input')

user_speed = st.number_input('Speed')

if user_input and user_speed:
    if st.button('Speak'):
        read_text(user_input, user_speed) 
    elif st.button('Stop'):
        stop_speech()
