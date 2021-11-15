import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import time
import wget
import howdoi
from googlesearch import search

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
print(" __      __        ")
print(" \ \    / /        ")
print("  \ \  / /_ _ _ __ ")
print("   \ \/ / _` | '__|")
print("     \  / (_| | |   ")
print("     \/ \__,_|_|   by arkal")



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, None, 10)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'var' in command:
                command = command.replace('var', '')
                print(command)
    except:
        pass
    return command


def run_var():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'close' in command:
        talk('Shutting down')
        exit()
    elif 'open' in command:
        talk('What program should i open?')
    elif 'brave' in command:
        os.system('brave.lnk')
    elif 'code' in command:
        os.system('code.lnk')
    elif 'virtual' in command:
        os.startfile(r'VirtualBox.lnk')
    elif 'download' in command:
        talk('Enter Url')
        url = input('Url: ')
        wget.download(url)
    elif 'name' in command:
        talk('My name is var, i was coded by master arkal, the best programmer in the world')
    elif 'email' in command:
        talk("Launching Email")
        os.startfile("outlook")
    elif 'sleep' in command:
        talk("Going to sleep")
        os.system("pause")
    elif 'google' in command:
        query = command.replace('google', '')
        for i in search(query):
            print(i)

    else:
        talk('Please say the command again.')



while True:
        run_var()
