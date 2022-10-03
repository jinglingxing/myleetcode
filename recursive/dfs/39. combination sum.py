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


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target_left: int, index: int):

            if target_left == 0:
                res.append(subset.copy())
                return

            for i, num in enumerate(candidates):
                if i < index:
                    continue
                if target_left >= 0:
                    subset.append(num)
                    dfs(target_left - num, i)
                    subset.pop()
                else:
                    return

        res = []
        subset = []
        dfs(target, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    sol.combinationSum([2, 3, 5], 8)

