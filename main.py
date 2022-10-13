from winsound import PlaySound
import speech_recognition as sr
import pywhatkit
import pyaudio
from playsound import playsound
from gtts import gTTS


# def speech(text):
#     print(text)
#     language = 'en'
#     output = gTTS(text=text, lang=language, slow=False)

#     output.save("./sounds/output.mp3")
#     PlaySound("./sounds/output.mp3")


def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print('say somthing....')
        playsound("./sounds/voicebooking-speech.wav")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"you said: {text}")
    return text


text = get_audio()

if 'youtube' in text.lower():
    pywhatkit.playonyt(text)
else:
    pywhatkit.search(text)
