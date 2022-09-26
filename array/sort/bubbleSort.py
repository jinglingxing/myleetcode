
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:26:12 2017

@author: Jinling
"""

def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                
list=[22,44,66,12,34,2,4,67,89,31]
bubbleSort(list)
print(list)