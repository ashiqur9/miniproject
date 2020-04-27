import speech_recognition as sr
from tempfile import TemporaryFile
import wave
import pygame
import pyglet
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignore any warning
warnings.filterwarnings('ignore')

# Record Audio and return as string
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
# ASsistant Response
def assistantresponse(text):
    #convert text to speech
    tts=gTTS(text=text,lang='en')
    tts.save("Hello.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Hello.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()


#A function for Wake Word phare
def wakeword(text):
    wake_word = ['siri', 'hey siri', 'hi siri']
    text = text.lower()
    for text in wake_word:
        return True
    return False
 # Function to current date
def getdate():
    now=datetime.datetime.now()
    my_day=datetime.datetime.today()
    weekday=calendar.day_name[my_day.weekday()]
    month=now.month
    daynum=now.day
    month_name=['January','February','March','April','May','June','July','Agust','September','October','November','December']
    originalnumber=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
    return('Today is '+weekday+' '+originalnumber[daynum-1]+' '+month_name[month-1]+'.')
# Random greeting
def greeting(text):
    greeting_input=['hi','hello','hola',"what's up"]
    greeting_response= ['Hi sir','How are you sir','Enjoy your day sir']
    for word in text.split():
        if word.lower() in greeting_input:
            return random.choice(greeting_response)+'.'

    return ''
# Wiki
def getperson(text):
    wordlist= text.split()
    return wikipedia.search(text)


while True:
    text=RecordAudio()
    response=''

    # Check wake word
    if(wakeword(text)==True):
        response=response+greeting(text)

        if('date' in text):
            response=response+' '+getdate()
        if('who is' in text):
            person=getperson(text)
            wiki=wikipedia.summary(person)

    print(response)
    assistantresponse(response)











