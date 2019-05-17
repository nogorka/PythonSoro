# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:57:50 2019

@author: Stephanie
"""

#answer=("Ахахах, о еде. $$удивление $$улыбка  В корпусе на первом этаже есть столовая и автомат с кофе, $$улыбка также прямо на остановке факультета есть киоск, выше по склону слата, и в библиотеке, где ты можешь ещё и почитать, есть столовая, где можно полноценно покушать.")

def search(text):
    
    for word in text.split():
        if word[:2:] =='$$':
            return word[2::]
    return "уточка"
#    answer[-1] = '@'
     
#def emoji(answer):
#    answer[-1] = '@'
#    while answer[-1] == '@':
#        search(answer)
#        
#        