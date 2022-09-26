#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:29:35 2020

@author: jinlingxing
"""

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]



   Hide Hint #1  
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
   Hide Hint #2  
For the two-sum problem, if we fix one of the numbers, say
x
, we have to scan the entire array to find the next number
y
which is
value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?
   Hide Hint #3  
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)-2):
            if (i==0) or (i> 0 and nums[i] != nums[i-1]):
                low = i+1
                high = len(nums)-1
                ssum = 0 - nums[i]
                
                while(low<high):
                    if nums[low]+nums[high] == ssum:
                        res.append([nums[i], nums[low], nums[high]])
                        #escape duplicates
                        while(low<high and nums[low] == nums[low+1]):
                            low+=1
                        while(low<high and nums[high] == nums[high-1]):
                            high-=1
                        low+=1
                        high-=1
                    elif nums[low] + nums[high] < ssum:
                        low+=1
                    else:
                        high-=1
        return res