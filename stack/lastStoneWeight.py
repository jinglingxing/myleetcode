#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:39:24 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem : 
    We have a collection of stones, each stone has a positive integer weight.

    Each turn, we choose the two heaviest stones and smash them together.
    Suppose the stones have weights x and y with x <= y.  
    The result of this smash is:

        If x == y, both stones are totally destroyed;
        If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

    At the end, there is at most 1 stone left.  
    Return the weight of this stone (or 0 if there are no stones left.)

Example :

    Input: [2,7,4,1,8,1]
    Output: 1
    Explanation: 
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
'''

from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            smash = y-x
            if smash != 0:
                stones.append(smash)

        if stones :
            return stones.pop()        
        return 0
        
#solution 2
    def lastStoneWeight2(self, stones: List[int]) -> int:
        while(len(stones) >= 1):
            x = sorted(stones)
            if len(x) < 2:
                return x[0]
            elif len(x) == 2:
                return x[1]-x[0]
            else:
                smash = x[-1]-x[-2]
                largest = x[-1]
                x.remove(largest)
                stones.remove(largest)
                sec_largest = x[-1]
                x.remove(sec_largest)
                stones.remove(sec_largest)
                x.append(smash)
                stones.append(smash)

if __name__=='__main__':
    sol = Solution()
    inp = [2,7,4,1,8,1]
    stones = inp.copy()
    out = sol.lastStoneWeight(stones)
    print("The solution to {} is : {}".format(inp, out))
