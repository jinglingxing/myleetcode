#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:35:33 2020

@author: jinlingxing
"""
'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle. 
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            row = []
            row.append(1) #row[0=1]
            for j in range(1, i): #i is the ith row
                row.append(res[i-1][j-1] + res[i-1][j]) #add sum ofthe two numbers directly above it
            row.append(1) #row[-1]=1
            res.append(row) #append the whole row to the result
        return res
    
sol = Solution()
numRows = 4
sol.generate(numRows)