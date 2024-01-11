import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox
from tkinter import *

def Audio_to_Text():
    r = sr.Recognizer()
    audio = 'audio.wav'
    with sr.AudioFile(audio) as source: 
        print('Say Something!')
        audio = r.record(source)
        print ('Done')
    try:
        text = r.recognize_google(audio)
        print(text)
    except Exception as e: 
        print(e)
            
def Speech_to_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            #r.pause_threshold = 3
            audio = r.listen(source,timeout=2,phrase_time_limit=5)
            text = r.recognize_google(audio, language = "vi-VN")
            txtSpeech.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            txtSpeech.insert(tk.END,"Could not understand audio\n")
        except sr.RequestError as e:
            txtSpeech.insert(tk.END,"Error :{}\n".format(e))
            
            
def reset_txtSpeech():  
    txtSpeech.delete("1.0",tk.END)
    
#GUI
root = tk.Tk()
root.title("Speech to Text")            
MainFrame = tk.Frame (root, bd = 20 , width = 600, height = 400)
MainFrame.pack()

LabelHeader = tk.Label(MainFrame, font = ('Time New Romans', 30,'italic'), text= 'Speech To Text' , width = 18)
LabelHeader.pack()

txtSpeech = tk.Text(MainFrame , font = ('arial', 15 ,'bold','italic'))
txtSpeech.pack()


ButtonHeader =tk.Button(MainFrame, font = ('Arial' , 12, 'bold'), text ='Speech To Text', width= 18, command = Speech_to_Text)
ButtonHeader.pack(side = tk.LEFT, padx = 5,pady = 25)

ButtonReset = tk.Button(MainFrame, font =('Arial', 12 ,'bold '), text = 'Reset to all',width = 18,command = reset_txtSpeech )
ButtonReset.pack(side = tk.RIGHT, padx = 5 , pady= 25)



root.mainloop()