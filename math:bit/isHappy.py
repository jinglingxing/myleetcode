#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:59:45 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem :
    Write an algorithm to determine if a number is "happy".

    A happy number is a number defined by the following process: 
    Starting with any positive integer, replace the number by the sum of the 
    squares of its digits, and repeat the process until the number equals 1 
    (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example :
    Input: 19
    Output: true
    Explanation: 
        1**2 + 9**2 = 82
        8**2 + 2**2 = 68
        6**2 + 8**2 = 100
        1**2 + 0**2 + 0**2 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        n1 = str(n)
        res = 0
        res_list = []
        res_list.append(n)
        while res != 1:
            res = 0
            for i in n1:
                res = res + int(i) * int(i) 
            if res in res_list:
                return False 
            res_list.append(res)
            n1 = str(res)
        return True
    
if __name__=='__main__':         
    sol = Solution()
    inp = 19
    out = sol.isHappy(inp)
    print("The solution to {} is : {}".format(inp, out))
