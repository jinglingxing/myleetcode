#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:31:48 2020

@author: jinlingxing
"""

'''
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

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        dic = {}
        count = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            else:
                count-=1
            if count == 0: #input: [0,1]
                max_len = i+1
            if count in dic:
                max_len = max(max_len, i-dic[count])
            else:
                dic[count] = i
        return max_len