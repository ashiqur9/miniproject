import requests
from bs4 import BeautifulSoup
import pafy
import vlc
import urllib
import speech_recognition as sr
from gtts import gTTS
import pygame

import webbrowser

def RecordAudio():
    r= sr.Recognizer()
    #Start microphone and start recording
    with sr.Microphone() as source:
        print('Say something!')
        audio= r.listen(source)
    # Use google speech recognition
    data =''
    try:
        data=r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError:
        print('Siri can\'t understand you sppech')
    except sr.RequestError as e:
        print('Siri request error: '+e)
    return data
def findYT(search):
    words = search.split()

    search_link = "http://www.youtube.com/results?search_query=" + '+'.join(words)
    search_result = requests.get(search_link).text
    soup = BeautifulSoup(search_result, 'html.parser')
    videos = soup.select(".yt-uix-tile-link")
    if not videos:
        raise KeyError("No video found")
    url = "https://www.youtube.com" + videos[0]["href"]
    webbrowser.open(url)


