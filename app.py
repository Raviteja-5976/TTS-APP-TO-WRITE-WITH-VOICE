import pyttsx3
import streamlit as st

engine = None
is_speaking = False  # Global variable to track the speech state

def preprocess_text(text, speed):
    # Preprocessing logic
    words = text.split()
    processed_text = []
    for word in words:
        if len(word) > 5:
            processed_text.append(f"{word} , {' , '.join(list(word))} \t {word}")
        else:
            processed_text.append(word)
    processed_text = '\n'.join(processed_text)
    processed_text = processed_text.replace('\n\n', '\n\nnext paragraph\n\n')
    return processed_text

def read_text(text, speed):
    # Read text logic
    global engine, is_speaking

    if engine is None:
        engine = pyttsx3.init()

    if not is_speaking:
        # Preprocess the text
        processed_text = preprocess_text(text, speed)

        # Speak the text
        engine.setProperty('rate', speed)
        engine.say(processed_text)
        engine.runAndWait()

        is_speaking = True

def stop_speech():
    # Stop speech logic
    global engine, is_speaking

    if engine is not None and is_speaking:
        engine.stop()
        is_speaking = False



st.title('WRITE WITH VOICE')
st.header('by Raviteja')

st.caption('THE SPEED DENOTES WORDS PER MINUTE')
st.caption('RECOMMENDED SPEED 120-180')

user_input = st.text_area('Input')

if (user_input==None) :
    st.caption('please fill the input space')

user_speed = st.number_input('Speed')

if (user_speed==None):
    st.caption('please enter the speed')

if user_input and user_speed:
    but=st.button('Speak')
    if but:
        read_text(user_input, user_speed) 
