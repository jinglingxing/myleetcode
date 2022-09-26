#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:05:47 2020

@author: jinlingxing
"""
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
'''

#solution 1
#we don't consider the output order
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        curr = []
        self.dfs(candidates, target, 0, curr, res)
        return res
        
    def dfs(self, candidates, target, s, curr, res ):
        if target == 0:
            res.append(curr.copy())
            return

        for i in range(s,len(candidates)):
            if candidates[i] > target:
                break
            curr.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, curr, res)
            curr.pop()

#solution 2
#The sets in the table are sorted in descending order      
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        curr = []
        for n in range(1, target//candidates[0]+1):
            self.dfs(candidates, target, 0, 0, n, curr, res)
        return res
        
    def dfs(self, candidates, target, s, d, n, curr, res ):
        if d == n:
            if target == 0:
                res.append(curr.copy())
                return

        for i in range(s,len(candidates)):
            if candidates[i] > target:
                break
            curr.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, d+1, n, curr, res)
            curr.pop()