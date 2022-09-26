# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 19:47:35 2017

@author: Jinling
"""

class binHeap:
    def __init__(self):
        self.heapList=[0]   #0 is the first item in heapList
        self.currentSize=0
    #if the current node is smaller than its parents node, swap them
    def nodeSwap(self, i):
        while i//2>0:
            if self.heapList[i]< self.heapList[i//2]:
                temp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=temp
            i=i//2
    #insert k into the list
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize=self.currentSize+1
        self.nodeSwap(self.currentSize)
    
  
    #swap the root node with the minimum child node
    def swapDown(self,i):
        while(i*2)<= self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]>self.heapList[mc]:
                temp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=temp
            i=mc
    #find the minimum child node

    def minChild(self,i):
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
            


    #delete node
    def delMin(self):
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.heapList.pop()
        self.swapDown(1)
        return retval
    

    def buildHeap(self,list):
      i = len(list) // 2
      self.currentSize = len(list)
      self.heapList = [0] + list[:]
      while (i > 0):
          self.swapDown(i)
          i = i - 1
        
bh = binHeap()
bh.buildHeap([44,482,303,822,23])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

        
            
            
    
    
    
    
    
    
    
    
    
    