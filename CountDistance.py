# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:15:50 2019
@author: Stephanie
"""
from SpeechRecognition import command
from TextToSpeech import gtalk

#работа с exel
import xlrd
rb = xlrd.open_workbook('схема.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

#списки вопросов и ответов
questions=[vals[rownum][0] for rownum in range(13)]
answers=[vals[rownum][1] for rownum in range(13)]
   
#current_question=command()
current_question="где магазины"



print(count_dist(current_question, questions))
print("вы сказали:", questions[pred_quest_num], "?")
print(answers[pred_quest_num])

gtalk(answers[pred_quest_num])#произносим ответ