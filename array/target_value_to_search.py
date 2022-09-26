#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:32:56 2020

@author: jinlingxing
"""

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = (start+end)//2
            if(nums[mid] == target):
                return mid
            if(nums[start] <= nums[mid]): #[4,5,6,7,0,1,2], 4 < (nums[mid] == 7)
                if(nums[start] <= target <= nums[mid]):
                    end = mid-1
                else:
                    start = mid+1
            else:#[4,5,6,0,1,2,3] nums[start] = 4, nums[mid] = 0, nums[end] =3
                if(nums[mid] <= target <= nums[end]):#target = 2
                    start = mid+1
                else:
                    end = mid-1
        return -1
            
