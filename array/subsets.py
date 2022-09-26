#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:52:15 2020

@author: jinlingxing
"""

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(n,s,curr):
            if n == len(curr):
                ans.append(curr.copy())
                return
            for i in range(s, len(nums)):
                curr.append(nums[i])
                dfs(n, i+1, curr)
                curr.pop()
        for i in range(0, len(nums)+1):
            dfs(i,0,[])
        return ans
                