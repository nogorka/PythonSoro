# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:09:14 2019

@author: Stephanie
"""

from CountDist import *
from Levenshtien import distance
import requests

#если вопрос не предзадан
def other(current_question):
    SERVER_URL = "http://192.168.43.143:8000/answer"
    r =requests.post(SERVER_URL, data={'question': current_question})
    answer = r.json()
    return answer

def cheak(current_question, questions, answers): 
    
    pred_quest_num, pred_quest_val=count_distance(current_question, questions)
#   номер предсказанного вопроса и значение

    two_sent_pointer=distance(current_question, questions[pred_quest_num])/len(questions[pred_quest_num])
    
#   счетчик переходы между предзадаными вопросами и не предзаданными
    if (two_sent_pointer < 0.6) or (pred_quest_val < 3):
        print("Возможно вы имели в виду:", questions[pred_quest_num], "?")
        return answers[pred_quest_num]
    else:
        return other(current_question)