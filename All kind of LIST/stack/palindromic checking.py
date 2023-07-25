# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:14:40 2017

@author: Jinling
"""



#  palindromic letter checking回文检测
import collections  

def palCheck(string):
    equal=True
    palDeque = collections.deque()
    for char in string:
        palDeque.appendleft(char)
    while palDeque.__len__()>1 and equal  :      
        front= palDeque.pop()
        rear = palDeque.popleft()        
        if front!= rear:
            return False
    return equal

print(palCheck("klakaljdlsjd"))
print(palCheck("abcba"))