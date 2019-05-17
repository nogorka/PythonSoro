# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:34:55 2019

@author: Stephanie
"""

from SpeechRecognition import command
from TextToSpeech import *
from Answer import cheak
from GIFsearch import *
import xlrd

def logics():
    rb = xlrd.open_workbook('схема.xlsx')
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

    #списки вопросов и ответов и выход из общения
    questions=[vals[rownum][0] for rownum in range(14)]
    answers=[vals[rownum][1] for rownum in range(14)]
    goodbyes=[vals[rownum][2] for rownum in range(12)]


    current_question=command()
#    current_question="не хочу жить, что будет когда я умру?"
#    current_question="где в корпусе столовая"

    #say("Привет, чем я могу помочь вам?")
    answer = cheak(current_question, questions, answers)
    
    emoji = search(answer)

    name = gtalk(answer)
    
    print(emoji, name, answer)
#    print("teacher_emoji/"+emoji+".gif")
    return emoji, name, answer


if __name__ == "__main__":
    logics()
    
    
#    def goodbye():
#  
#        for goodbye in goodbyes:
#            if current_question==goodbye:
#                answer = gtalk(goodbye, "жду тебя в следующий раз")
#                flag = False
#        break