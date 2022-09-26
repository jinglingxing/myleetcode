# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 19:09:41 2017

@author: Jinling
"""

def selectionSort(list):
    for slot in range(len(list)-1,0,-1):
        posOfMax=0
        for location in range(1, slot+1):
            if list[location]> list[posOfMax]:
               posOfMax=location
        temp=list[slot]
        list[slot]=list[posOfMax]
        list[posOfMax]=temp
list=[1,33,22,34,12,78,21,62,5,7,55,99,43]
selectionSort(list)
print(list)

