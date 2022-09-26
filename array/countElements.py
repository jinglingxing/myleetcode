#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:46:46 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem : 
    Given an integer array arr, count element x such that x + 1 is also in arr.
    If there're duplicates in arr, count them seperately.

Example 1 :
    Input: arr = [1,2,3]
    Output: 2
    Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2 :
    Input: arr = [1,1,3,3,5,5,7,7]
    Output: 0
    Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

Example 3 :
    Input: arr = [1,3,2,3,5,0]
    Output: 3
    Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Example 4 :
    Input: arr = [1,1,2,2]
    Output: 2
    Explanation: Two 1s are counted cause 2 is in arr.

'''

from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        S = []
        count = 0
        for i in arr:
            S.append(i+1)
        for x in S:
            if x in arr:
                count += 1
        return count
        
        
        
if __name__ == "__main__":
    sol = Solution()
    inp = [1,3,2,3,5,0]
    out = sol.countElements(inp)
    print("The solution to {} is : {}".format(inp, out))