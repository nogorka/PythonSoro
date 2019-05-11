# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:37:21 2019

@author: Stephanie

current_qeustion-текущий вопрос
cur_word-слово из текущего вопроса
question-вопрос из списка вопросов
word-слово из вопроса
quest_num-список расстояний между каждым словом из текущего вопроса и словом из вопроса из списка
question_koef-список расстояний между текущим вопросом и всеми остальными
"""
from Levenshtien import distance

def count_distance(current_question, questions):
    quest_num,question_koef=[],[]
    
    for cur_word in current_question.split():
        for question in questions:
            _n=0
            for word in question.split():
                _n=_n+distance(cur_word, word)
            quest_num.append(_n/len(question))
#           находим расстояние между каждым словом cur_question и всеми вопросами
    
    size=len(quest_num)//len(current_question.split()) #длина question_koef 
      
    for i in range(size):
        question_koef.append(0)
        for j in range(len(current_question.split())):
            question_koef[i]+=quest_num[i]
#           нахождение расстояния по словам для вопросов
            
    i=0
    for question in questions:
        question_koef[i]+=(distance(current_question, question)/len(question))
        i+=1
#       нахождение расстояния по фразам и прибавление

#    print(question_koef, min(question_koef))
    return question_koef.index(min(question_koef)), min(question_koef)#предсказаный вопрос
