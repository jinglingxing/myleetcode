# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:55:59 2017

@author: Jinling
"""


import Queue
 


def hotPotato(namelist, num):
    simqueue = Queue.Queue()
    for name in namelist:
        simqueue.put(name)
    while simqueue.qsize()>1:
        for i in range(num):
            simqueue.put(simqueue.get())
        simqueue.get()
    return simqueue.get()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
        
        