# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:43:13 2019

@author: Stephanie
"""

from gtts import gTTS
import os

def talk(words):
	os.system("say " + words)

def gtalk(words):
    tts = gTTS(text=words, lang="ru", lang_check = False)
    tts.save("good.mp3")
    #os.system("mpg321 good.mp3")
    os.startfile("good.mp3")

def say(words):   
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    
      
if __name__ == "__main__":
    talk("Привет, чем я могу помочь вам?")