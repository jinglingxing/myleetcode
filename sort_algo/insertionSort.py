# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 19:20:16 2017

@author: Jinling
"""

def insertionSort(list):
    for index in range (1,len(list)):
        curValue= list[index]
        position= index
        while position>0 and list[position-1]>curValue:
            list[position]=list[position-1]
            position=position-1
        list[position]=curValue
list=[5,3,2,7,99,44,22,81,32]
insertionSort(list)
print(list)       