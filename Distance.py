# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:15:50 2019

@author: Stephanie
"""

def distance(a, b):
    "Растояния Левенштейна между a и b"
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1) 
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]
  
import xlrd
rb = xlrd.open_workbook('схема.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

questions=[vals[rownum][0] for rownum in range(13)]
answers=[vals[rownum][1] for rownum in range(13)]
#print(questions)
#print(answers)
       
#current_question='есть ли социальная стипендия '
current_question=input("enter question:" )
quest_num=[]   
question_koef=[] 
for cur_word in current_question.split():
    
    _koef=0
    for question in questions:
        _n=0
        for word in question.split():
            _n=_n+distance(cur_word, word)
        quest_num.append(_n)#находим расстояние между каждым словом cur_question и всеми вопросами
        
size=len(quest_num)//len(current_question.split())  
  
for i in range(size):
    question_koef.append(0)
    for j in range(len(current_question.split())):
        question_koef[i]+=quest_num[i]

pred_quest_num=question_koef.index(min(question_koef))
print("вы сказали:", questions[pred_quest_num], "?")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
