import speech_recognition as sr 
import time 

r = sr.Recognizer()
    
with sr.AudioFile('C:\PythonProject\\tamtam.wav') as source: 
        print('Listening!!!!')
        audio = r.listen(source)
        print ('Done')
try:
        text = r.recognize_google(audio, language = 'en-US')
        time.sleep(1.5)
        print("Waiting for translating....\n")
        print(text)
except Exception as e: 
        print(e)