

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 14:45:48 2017

@author: Jinling
"""

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def draw(myTurtle, length):
    if length >0:
        myTurtle.forward(length)
        myTurtle.right(90)
        draw(myTurtle, length-3)
draw(myTurtle,200)
myWin.exitonclick()

