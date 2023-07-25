#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:13:06 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust and N == 1: #N=1, trust =[], there's a judge
            return 1
        l_points = [0]*(N+1)
        for t in trust :
            l_points[t[0]]=l_points[t[0]]-1 #if we trust someone, we lose points
            l_points[t[1]]=l_points[t[1]]+1 #if we are trusted, we get points
        for i in range (len(l_points)):
            if l_points[i]==N-1: #judge gets N-1 points
                return i
        return -1
        
    
    
sol = Solution()
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
sol.findJudge(N, trust)