# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:57:50 2019

@author: Stephanie
"""

answer=("Ахахах, о еде.   В корпусе на первом этаже есть столовая и автомат с кофе, $$улыбка также прямо на остановке факультета есть киоск, выше по склону слата, и в библиотеке, где ты можешь ещё и почитать, есть столовая, где можно полноценно покушать. $$удивление")

def search(text):
    
    for word in text.split():
        if word[:2:] =='$$':
#            flag=False
#    if flag==False:
#        return text.pop()
            return word[2::]," ".join(text.split()[:-1:])

    return "уточка", text

if __name__ == "__main__":
    print(search(answer))
#    answer[-1] = '@'
     
#def emoji(answer):
#    answer[-1] = '@'
#    while answer[-1] == '@':
#        search(answer)
#        
#        