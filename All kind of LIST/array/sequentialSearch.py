# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:52:01 2017

@author: Jinling
"""

def orderedSequentialSearch(list,item):
    pos= 0
    found=False
    stop=False
    while pos<len(list) and not found and not stop:
        if list[pos]==item:
            found= True
        else:
            if list[pos]> item:
                stop= True
            else:
                pos=pos+1
        return found
    
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))
            
            