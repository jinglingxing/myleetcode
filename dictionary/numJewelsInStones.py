#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:44:08 2020

@author: jinlingxing
"""
'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic = {}
        i=0
        while i<len(J):
            dic[J[i]] = i #key is letters in J, and value is index
            i+=1
        count = 0
        j=0
        while j<len(S):
            if S[j] in dic:
                count += 1
            j+=1
        return count