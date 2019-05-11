# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:34:55 2019

@author: Stephanie
"""
from SpeechRecognition import command
from CountDist import *
from TextToSpeech import gtalk
import xlrd
import requests


def other():
    SERVER_URL = "http://192.168.43.143:8000/answer"
    r =requests.post(SERVER_URL, data={'question': current_question})
    answer = r.json()
    return answer



rb = xlrd.open_workbook('схема.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

#списки вопросов и ответов
questions=[vals[rownum][0] for rownum in range(13)]
answers=[vals[rownum][1] for rownum in range(13)]

current_question=command()
#current_question="где магазины "

pred_quest_num=count_distance(current_question, questions)
#номер предсказанного вопроса


if pred_quest_num>3:#добавить анализ двух вопросов чтобы было двойное условие
    answer=other()
else:
    print("возможно вы имели в виду:", questions[pred_quest_num], "?")
    answer=answers[pred_quest_num]
print(answer)
#gtalk(answer)#произносим ответ