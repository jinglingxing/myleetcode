#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:46:58 2020

@author: jinlingxing
"""
'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zero = 0
        num_one = 0
        num_two = 0
        for i in nums:
            if i == 0:
                num_zero += 1
            elif i == 1:
                num_one += 1
            else:
                num_two += 1
           
        for i in range(0, num_zero):        
            nums[i] = 0
        for i in range(num_zero, num_zero+num_one):
            nums[i] = 1
        for i in range(num_zero+num_one, num_zero+num_one+num_two):
            nums[i] = 2