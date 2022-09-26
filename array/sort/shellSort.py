# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 20:44:30 2017

@author: Jinling
"""

#希尔排序

def shellSort(alist):
    sublistCount=len(alist)//2
    while sublistCount>0:
        for sp in range(sublistCount):  #sp==start position
            gapInsertionSort(alist, sp,sublistCount)
        print("after increments of size ", sublistCount,
              "the list is ", alist)
        
        sublistCount=sublistCount//2
        


        
        
def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
       
        curValue=alist[i]
        position = i
         
        while position>= gap and alist[position-gap]>curValue:
            alist[position]=alist[position-gap]
            position=position-gap
             
        alist[position]=curValue
alist = [54,26,93,17,77,31,44,55,20]

shellSort(alist)

print(alist)
            
    