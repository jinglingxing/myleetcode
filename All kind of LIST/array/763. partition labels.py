#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:40:06 2020

@author: jinlingxing
"""

class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
    
sol = Solution()
S = "ababcbacadefegdehijhklij"
sol.partitionLabels(S)
print(sol.partitionLabels(S))