# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:34:55 2019

@author: Stephanie
"""
from SpeechRecognition import command
from TextToSpeech import gtalk
from Answer import cheak
import xlrd
  
rb = xlrd.open_workbook('схема.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

#списки вопросов и ответов
questions=[vals[rownum][0] for rownum in range(13)]
answers=[vals[rownum][1] for rownum in range(13)]

current_question=command()
#current_question="где магазины"

answer=cheak(current_question, questions, answers)
    
print(answer)
gtalk(answer)#произносим ответ