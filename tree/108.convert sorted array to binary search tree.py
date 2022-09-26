#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:02:46 2020

@author: jinlingxing
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        left_list = nums[0:mid]
        right_list = nums[mid+1:]
        root.left = self.sortedArrayToBST(left_list)
        root.right = self.sortedArrayToBST(right_list)
        return root