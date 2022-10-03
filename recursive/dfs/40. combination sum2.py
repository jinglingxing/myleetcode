#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:46:28 2020

@author: jinlingxing
"""
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.dfs(candidates, target, 0, [], ans)
        return ans
    
    def dfs(self, candidates, target, s, curr, ans):
        if target == 0:
            ans.append(curr.copy())
            return
        
        for i in range(s, len(candidates)):
            if candidates[i] > target:
                break
            if i > s and candidates[i] == candidates[i-1]: #remove duplicates
                continue
            curr.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i+1, curr, ans)
            curr.pop()
        