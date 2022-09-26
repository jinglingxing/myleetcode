# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 13:10:52 2017

@author: Jinling
"""

def binarySearch(list, item):
    if len(list)==0:
        return False
    else:
        midpoint= len(list)//2
        if list[midpoint]==item:
            return True
        else:
            if item<list[midpoint]:
                return binarySearch(list[:midpoint], item)
            else: 
                return binarySearch(list[midpoint+1:], item)
            
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
            