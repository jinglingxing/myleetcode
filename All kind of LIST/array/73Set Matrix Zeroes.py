#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:50:49 2020

@author: jinlingxing
"""
matrix = [[1,1,1],[1,0,1]]
rows = len(matrix)
columns = len(matrix[0])
R, C = set(), set()
for r in range(0,rows):
    for c in range(0,columns):
        if matrix[r][c] == 0:
            R.add(r)
            C.add(c)

for r in range(0,rows):
    for c in range(0,columns):
        if r in R or c in C:
            matrix[r][c] = 0
        
            