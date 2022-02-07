import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser #It will launch web application such as websites
import smtplib #It will enable to send email
import os #This will launch system applications
import re #This will help to read files.

engine = pyttsx3.init() #pyttsx is a text-to-speech conversation library
voices = engine.getProperty('voices') #From this we will get voices from our computer
engine.setProperty('voice',voices[0].id) #Zero index means to choose between different sound voices such as Male or Female  

#This Function will take take one parameter in which It will speak as per user's speech.  
def speak(audio):
    engine.say(audio) #This will speak whatever user will speak
    engine.runAndWait() #This function will wait and then after give output as a speech

#This will take input from microphone and returns string output
def takeCommand():
    rec = sr.Recognizer() #This function will recognize user input
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 0.5 #This will control pause timing after speak, we can also change it to 0, 0.5 & so on.
        audio = rec.listen(source) #This will converts speech and return string and save into audio variable for further speech process (To translate string into user understandable output).

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language='en-in') #This is google's engine which recognizes user's voice and give appropriate output.
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query

#Send mail function will send email to your friend
def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo() #Identify iteself when connecting to another email server to start the process of sending mail.
    server.starttls() #Upgrade plain text into an encrypted (TLS or SSL) connection.

    server.login('srenil0653@gmail.com', Password_here)
    server.sendmail('srenil0653@gmail.com', to, content)

    server.close()

#This function will wish user as per current time
def wishMe():
    Hour = int(datetime.datetime.now().hour)
    if Hour >= 0 and Hour < 12:
        speak("Good morning!")

    elif(Hour >= 12 and Hour < 17):
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("Hello, I am Your assistant. How may I help you!")

#This is main function from this program will start
if __name__  == "__main__":
    # wishMe()

    while True:
        query = takeCommand().lower()
        #Logic for executing task based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2) #It will return 2 sentences from wikipedia

            speak('According to wikipedia')
            speak(results)

        elif "open youtube" in query:
            webbrowser.get().open("http://www.youtube.com")

        elif "open google" in query:
            webbrowser.get().open("http://www.google.com")

        elif "open paytm" in query:
            codePath = '//Applications//paytm.app'
            os.startfile(codePath)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strTime}")

        elif "contacts" in query:
            speak('Which contact do you want to search, please tell the name: ')
            records = read_vcf()
            print(records)

        elif "send email" in query:
            try:
                speak("Tell me the content of your email: ")
                content = takeCommand()

                to = 'sonirenil12@gmail.com'
                send_mail = sendMail(to,content)
                speak("Email has been send")

            except Exception as e:
                print(e)
                speak("Sorry, try again later!!")