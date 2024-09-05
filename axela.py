import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui


listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
  engine.say(text) 
  engine.runAndWait()
  
def take_command():
 try :
     with sr.Microphone()as source:
        print('listening..')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command=command.lower()
        if 'alexa'in command:
         command=command.replace('alexa','')
         print(command)
 except:
     pass
 return command

talk('hello')
talk('i am alexa')
talk('how can i help you ')

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search for' in command:
        person = command.replace('search for','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'love you' in command:
        talk('i also you sai ram darling ')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'who are you' in command:
        talk('I am a virtual assistant created by maveen')
    elif 'open' in command:
         search = command.replace('open','')
         talk(search)
         pywhatkit.search(search)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'send' in command:
        talk('pelse enter a phone number:')
        p_number=input(' pelse enter the phone number:')
        talk('enter the message do you whant to send:')
        message=input('enter the message:')
        talk('enter time in hours as in 24 hours formate:')
        time=int(input('enter time in hr:'))
        talk('enter time in minutes as in 24 hours formate:')
        min=int(input('enter time in min:'))
        pywhatkit.sendwhatmsg(p_number,message,time,min)
    elif 'speed test'in command:
        import time
        start =time.time()
        i=1
        while i<=1000000:
            i+=1
        end=time.time()
        talk(end)
        print(end-start)
    elif 'exit' in command:
        talk('ok thankyou ')
        exit()
    elif 'increase the volume' in command:
        pyautogui.press("volumeup",100)
    else:
     talk('Please say the command again.')
while True:
    run_alexa()