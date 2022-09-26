# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 21:59:24 2017

@author: Jinling
"""

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:       
        sp=partition(alist,first,last) #sp==split point
        quickSortHelper(alist,first,sp-1)
        quickSortHelper(alist,sp+1,last)

def partition(alist, first,last): 
           
    pivotvalue= alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<= pivotvalue:
            leftmark=leftmark+1
            
        while alist[rightmark]>= pivotvalue and rightmark>=leftmark:
            rightmark=rightmark-1
        if rightmark<leftmark:
            done=True
        else:
            temp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=temp
            

            
    temp=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=temp
    
    return rightmark
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
    