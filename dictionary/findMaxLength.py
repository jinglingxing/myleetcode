#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:32:49 2020

@author: jinlingxing & luc michea
"""

'''
Problem:
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000. 
'''
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        dic = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1
            if count == 0:
                max_len = i+1
            if count in dic:
                max_len = max(max_len, i - dic[count])
            else:
                dic[count] = i
        return max_len
sol = Solution()
nums = [0,0,1,0,0,0,1,1]
sol.findMaxLength(nums)
