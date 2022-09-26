#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:12:47 2020

@author: jinlingxing
"""
'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
'''
from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if len(A[0])%2 ==1 :
                    if j <= len(A[0])//2:
                        temp = A[i][j]
                        A[i][j] = abs(A[i][len(A[0])-1-j] -1)
                        A[i][len(A[0])-1-j] = abs(temp-1)
                        
                if len(A[0])%2 == 0 :
                    if j < len(A[0])//2:
                        temp = A[i][j]
                        A[i][j] = abs(A[i][len(A[0])-1-j] -1)
                        A[i][len(A[0])-1-j] = abs(temp-1)
        return A
    
sol= Solution()
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
sol.flipAndInvertImage(A)