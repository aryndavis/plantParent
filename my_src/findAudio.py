from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import os


def find_lyrics(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, show_all=True)
        print(text)


find_lyrics('output.wav')
