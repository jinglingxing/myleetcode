# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 12:22:13 2017

@author: Jinling
"""

def moveTower(n,fromPole, toPole, buffer):
    if n >=1:
      
        moveTower(n-1, fromPole, buffer, toPole)
        print ("777")
        movedisk(fromPole, toPole)
        print ("888")
        moveTower(n-1, buffer, toPole, fromPole)
        print ("999")
def movedisk (fp,tp):
    print ("moving disk from" ,fp, "to ",tp)

moveTower(3,"a","b","c")