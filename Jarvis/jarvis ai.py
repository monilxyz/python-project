import speech_recognition as sr
import webbrowser
import os
from win32com.client import Dispatch
import datetime
speak = Dispatch("SAPI.SpVoice").Speak

# while 1:
#     s=input()
#     speak(s)
def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak:')
        r.pause_threshold=1
        audio = r.listen(source)
        query=r.recognize_google(audio)
        sites=[['youtube','https://youtube.com'],['facebook','https://facebook.com'],
               ['instagram','https://instagram.com']]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f'opening {site[0]} sir')
                webbrowser.open(site[1])
        if f"thousand years".lower() in query.lower():
                path = "c:/Users/monil/Desktop/projects/python/1.mp3"
                os.system(path)
        if f"play begging".lower() in query.lower():
                speak('playing beggin sir')
                webbrowser.open('https://www.youtube.com/watch?v=Qdkt3I5-FG4')
        if f"the time".lower() in query.lower():
                strtiem = datetime.datetime.now().strftime("%H:%M:%S")
                speak(strtiem)
        print(query)
        return query
text=takecom()
# speak(text)    

