#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:05:08 2020

@author: jinlingxing
"""

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        ans = []
        self.dfs(nums, k, 0, [], ans)
        return ans
    
    def dfs(self, nums, m, s, curr, ans):
        if len(curr) == m:
            ans.append(curr.copy())
            return
        
        for i in range(s, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, m, i+1, curr, ans)
            curr.pop()