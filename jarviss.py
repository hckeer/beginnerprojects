import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id )

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            
                
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        talk(song)
        
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S:%p')
        talk(time)
        
        
        print(time)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'where is' in command:
        thing = command.replace('where is ', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)

        
    elif 'what is' in command:
        thing = command.replace('what is ', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(talk)
    elif 'date' in command:
        talk('I am in relationship with IAM')
        
    elif 'are you single' in command:
        talk('I am in relationship with IAM')
    elif 'who is aayas' in command:
        talk('aayas is black boy')
        
    else:
        talk('please speak my friend, You can speak to me, I am your everything')
        print(talk)
        



        
while True:
    run_alexa()


