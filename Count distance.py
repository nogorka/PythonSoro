# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:15:50 2019

@author: Stephanie

current_qeustion-текущий вопрос
cur_word-слово из текущего вопроса
question-вопрос из списка вопросов
word-слово из вопроса
quest_num-список расстояний между каждым словом из текущего вопроса и словом из вопроса из списка
question_koef-список расстояний между текущим вопросом и всеми остальными
"""
from SpeechRecognition import command
from Levenshtien import distance
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
current_question="рядом магазины"
quest_num,question_koef=[],[]

for cur_word in current_question.split():
    for question in questions:
        _n=0
        for word in question.split():
            _n=_n+distance(cur_word, word)
        quest_num.append(_n)
        #находим расстояние между каждым словом cur_question и всеми вопросами


size=len(quest_num)//len(current_question.split()) #длина question_koef 
  
for i in range(size):
    question_koef.append(0)
    for j in range(len(current_question.split())):
        question_koef[i]+=quest_num[i]

pred_quest_num=question_koef.index(min(question_koef))#предсказаный вопрос
print("вы сказали:", questions[pred_quest_num], "?")


print(answers[pred_quest_num])

gtalk(answers[pred_quest_num])
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
