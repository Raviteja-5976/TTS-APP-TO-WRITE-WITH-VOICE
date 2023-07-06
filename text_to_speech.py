import pyttsx3

# engine = pyttsx3.init()

def preprocess_text(text, speed):
    # Preprocessing logic
    words = text.split()
    processed_text = []
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
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
    # Preprocess the text
    processed_text = preprocess_text(text, speed)

    # Speak the text
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    engine.say(processed_text)
    engine.runAndWait()

def stop_speech( ):
    # Stop speech logic
    # Stop the speech engine
    engine= pyttsx3.init()
    engine.stop()
