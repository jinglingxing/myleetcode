# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:30:23 2017

@author: Jinling
"""

import random
import Queue 

               
class Task(object):
    def __init__(self, time):
        self.timeStamp = time
        self.page = random.randrange(1,21) #random numbers from 1-21 represents pages 
    def getPage(self):
        return self.page
    def waitTime(self,curtaskTime):
        ##curtaskTime is the current timestamp
        return curtaskTime -self.timeStamp
      

class Printer(object):
    #initialization
    
    def __init__(self, timeperpage):
        #print one page, need what time
        self.curtask = None
        self.timeRemaining = 0
        self.timeperpage = timeperpage
    
    
    #the constructor of the task
    def startTask(self,newTask):  
        self.curtask = newTask
        
        self.timeRemaining = newTask.getPage() * self.timeperpage 
       
              
    #if the printer is busy 
    def busy(self):
        if self.curtask != None:
            return True
        else:
            return False
    
    def PrintTask(self):
        if self.curtask != None:
            self.timeRemaining -=1
            if self.timeRemaining <= 0:
                self.curtask = None
def Simulation(totalTime,timeperpage):

    labPrinter = Printer(timeperpage)
    printQueue = Queue.Queue()

    waitingTime = []  #every task waiting time
        
    for curSeconds in range(totalTime):
        num = random.randrange(1,181)  #generate random number 
        if num == 1:
            task = Task(curSeconds)     #generate new task
            printQueue.put(task)    #new task enter the queue
        if (not labPrinter.busy()) and (not printQueue.empty()):
                #printer is not busy and has tasks for waiting
            newTask = printQueue.get()  #push next task
            waitingTime.append(newTask.waitTime(curSeconds))  # remember the waiting time
            labPrinter.startTask(newTask)  #reload the new task
        labPrinter.PrintTask()  
            
    avgWaitTime = sum(waitingTime)/ len(waitingTime)
    return avgWaitTime
       
        

def main():

    timeperpage = 5
    totalTime = 36000
    for i in range(10):
        avgTime =Simulation(totalTime,timeperpage)
        print ("average print time is %.5f seconds" %avgTime)
        
        
if __name__ == "__main__":
    main()