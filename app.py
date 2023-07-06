import pyttsx3
import streamlit as st
from pydub import AudioSegment

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
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)

    # Preprocess the text
    processed_text = preprocess_text(text, speed)

    # Speak the text
    engine.save_to_file(processed_text, 'output.wav')
    engine.runAndWait()

    # Convert WAV to MP3
    audio = AudioSegment.from_wav('output.wav')
    audio.export('output.mp3', format='mp3')

# Streamlit app
st.title('WRITE WITH VOICE')
st.header('by Raviteja')

st.caption('THE SPEED DENOTES WORDS PER MINUTE')
st.caption('RECOMMENDED SPEED 120-180')

user_input = st.text_area('Input')

if user_input:
    user_speed = st.number_input('Speed')
    if user_speed:
        if st.button('Speak'):
            read_text(user_input, user_speed)
            st.audio('output.mp3', format='audio/mp3')
