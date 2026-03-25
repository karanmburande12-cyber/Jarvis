import pyttsx3
import speech_recognition as sr
import random
import webbrowser
from datetime import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import smtplib

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # change index here
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            content =  r.recognize_google(audio, language='en-in')         
            print("You said......... " + content)
        except Exception as e:
            print("Please try again...")

    return content    


def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Welcome, How can I help you.")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,4)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=n_FCrCQ6-bA&list=RDn_FCrCQ6-bA&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=IOcGS4D1tM0&list=RDIOcGS4D1tM0&start_radio=1")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=8of5w7RgcTc&list=RD8of5w7RgcTc&start_radio=1")
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=trTlXJXtxMI&list=RDtrTlXJXtxMI&start_radio=1") 
        elif "say time" in request:
            now_time = datetime.now().strftime("%H:%M")
            speak("Current time is " + now_time)

        elif "say date" in request:
            now_date = datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + now_date)
       
        elif "new task" in request:
            task = request.replace("new task ", "")   
            task = task.strip() 
            if task != "":
                speak("Adding task "+ task)
                with open("todo.txt", "a")as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            with open("todo.txt", "r")as file:
                speak("work we have to dotoday is : "+ file.read())

        elif "show work" in request:
            with open("todo.txt", "r") as file:
                tasks = file.read()
                notification.notify(
                    title = "Today's wokk",
                    message = tasks
                )


        elif "open youtube"in request:
            webbrowser.open("www.youtube.com")

        elif "open"in request:
            query = request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")


        elif "wikipedia search"in request:
            request = request.replace("jarvis","")
            request = request.replace("search wikipedia ", "")
            print(request)
            result=wikipedia.summary(request, sentences=1)
            speak(result)


        elif "google"in request:
            request = request.replace("jarvis","")
            request = request.replace("google search ", "")
            webbrowser.open("https://www.google.com/search?q="+request)
        
        elif "send whatsapp"in request:
            pwk.sendwhatmsg("+919623831453","Hi ,How are you",23,52, 30)

        
       
        elif "stop" in request or "exit" in request:
            speak("Stopping the program. Goodbye.")
            break



main_process()