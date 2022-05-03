import cv2
import os
import sys
import time
import operator
import requests
import pyautogui  
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit as wk
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Ready To Comply. What can I do for you?")   

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening....")
       r.pause_threshold = 1
       audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis'in query:
            print("yes sir")
            speak("Hey sir")              
        elif "who are you" in query:
            print("My name is Jarvis")
            speak('My name is Jarvis and I am little sister of Iron man Jarvice')
            print('Nice to meet you')
            speak('Nice to meet you') 
        elif "who created you" in query:
            print("Reetika Anand created me")
            speak("Reetika Anand created me and exploited me")
        
        elif 'what is' in query:
            speak('Searching Wikipedia....')
            query = query.replace("What is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'just open google' in query:
            webbrowser.open('google.com')
            #npath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\chrome.exe"
            #os.startfile(npath)

        elif 'open google' in query:
            speak("What should I search?")
            qry = takeCommand().lower()
            webbrowser.open(f"{query}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak("what you will like to watch?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")   
           
        
        elif "open notepad" in query:
            npath = "C:\Windows\System32\\notepad.exe"
            os.startfile(npath) 
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")  
        elif "open paint" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')

        elif "open command promt" in query:
            os.startfile("start cmd") 
        elif "close command promt" in query:
            os.system("taskkill /f /im cmd.exe")  

        elif 'type' in query:
            query = query.replace("type", "")
            pyautogui.typewrite(f"{query}", 0.1)   

        elif 'draw a line' in query:
            pyautogui.moveTo(x=400, y = 300, duration=1)
            pyautogui.leftClick
            pyautogui.dragRel(400, 0, 1) 

        elif 'draw a square' in query:
            pyautogui.moveTo(x=1000, y=300, duration=1)
            pyautogui.leftClick
            distance = 400
            pyautogui.click();
            pyautogui.dragRel(distance, 0, duration=1)
            pyautogui.dragRel(0, distance, duration=1) 
            pyautogui.dragRel(-distance, 0, duration=1) 
            pyautogui.dragRel(0, -distance, duration=1)   
        elif 'red colour' in query:
            pyautogui.moveTo(x=970, y=76, duration=1)
            pyautogui.click(x=970, y=76, clicks=1, interval=0, button='left')

        elif "draw rectangular sipral" in query:
            pyautogui.moveTo(x=400, y=300, duration=1)
            pyautogui.leftClick
            distance=300
            while distance > 0:
                pyautogui.dragRel(distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, distance, 0.1, button="left")
                pyautogui.dragRel(-distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, -distance, 0.1, button="left")

        elif "close paint" in query:
            os.system("taskkill /f /im /mspaint.exe")

        elif "undo" in query:
            pyautogui.hotkey('ctr' ,'z')

        elif "redo" in query:
            pyautogui.hotkey('ctrl', 'y')    

        elif "refresh" in query:
            pyautogui.hotkey('ctrl', 'r') 

        
        elif "open a new window" in query:
            pyautogui.hotkey('ctrl', 'n')     

        elif "open a new window in Incognito mode" in query:
            pyautogui.hotkey('ctrl','shift', 'n') 

        elif "open a new tab" in query:
            pyautogui.hotkey('ctrl','t')    

        elif "Jump to the next open tab" in query:
            pyautogui.hotkey('ctrl','tab')  

        elif "Jump to the previous open tab" in query:
            pyautogui.hotkey('ctrl','shift','tab') 

        elif "Open your home page in the current tab" in query:
            pyautogui.hotkey('Alt', 'home') 

        elif "close the current tab" in query:
            pyautogui.hotkey('Ctrl', 'w')   

        elif "Close the current window" in query:
            pyautogui.hotkey('ctrl','shift','w')

        elif "Minimize the window" in query:
            pyautogui.hotkey('alt','shift','n')

        elif "Maximize the window" in query:
            pyautogui.hotkey('alt','f','x')  

        elif "Open the History page in a new tab" in query:
            pyautogui.hotkey('ctrl', 'h')    

        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift','delete')                                                

#        elif "play music" in query:
#           music_dri = 'This PC\Music'            
#          songs = os.listdir(music_dri) 
#            os.startfile(os.path.join(music_dri, random.choice(songs)))
#        elif "close music" in query:
#            os.system("taskkill /f /im vlc.eve")               

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")           
            speak(f"The time is {strTime}")   

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")    

        elif 'lock the system' in query:
            os.system("rundl123.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'hibernate the system' in query:
            os.system("rundl123.exe powrprof.dll,SetSuspendState 0,1,0")    

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)    
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()   

        elif "go to sleep" in query:
            speak('alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"(name).png")
            speak("screenshot taken and saved")             
            pyautogui.hotkey('win' ,'ptr scr')
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divide' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split()))) 

        elif "whats my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text         
                print(ipAdd)
                speak("your ip address is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again later")    

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")            
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")       
            pyautogui.press("volumedown")     
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")

        elif "mute" or "unmute" in query:
            pyautogui.press("volumemute")
