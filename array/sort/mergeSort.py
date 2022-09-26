# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 21:24:09 2017

@author: Jinling
"""

#归并排序
def mergeSort(alist):
    print("splitting",alist)
    if len(alist)>1:#if the list <1, then the list is sorted
        mid = len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        #merge
        i=0
        j=0
        k=0
        while i< len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j< len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
    print("merge",alist)
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
            
        