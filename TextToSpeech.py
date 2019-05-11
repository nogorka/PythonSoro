# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:43:13 2019

@author: Stephanie
"""

from gtts import gTTS
import os


# Функция, позволяющая проговаривать слова
def talk(words):
	print(words) # Дополнительно выводим на экран
	os.system("say " + words) # Проговариваем слова
    
    
# Вызов функции и передача строки именно эта строка будет проговорена компьютером
talk("Привет, чем я могу помочь вам?")


def gtalk(words):
    tts = gTTS(text=words, lang="ru", lang_check = False)
    tts.save("good.mp3")
    #os.system("mpg321 good.mp3")
    os.startfile("good.mp3")