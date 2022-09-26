# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:41:15 2017

@author: Jinling
"""
import Stack 


def paircheck(symbol):
    s = Stack.Stack()
   
    isPair = True
    index = 0
    while index < len(symbol) and isPair:
        symbol1= symbol[index]
        
        if symbol1 in "([{":
            s.push(symbol1)
            #error:ValueError: substring not found
            #实参symbol1 和形参symbol名字过于相似
        elif s.isEmpty():
            isPair = False
           
        else:
            top= s.pop()
            if not match(top , symbol1):
                isPair = False
                print "rfs"
                
        index+=1
    if isPair and s.isEmpty():
        return True
    else:
        return False
    

def match(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(paircheck('{{([][])}()}'))
print(paircheck('[{()]'))