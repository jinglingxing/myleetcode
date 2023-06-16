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
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        left_branch = nums[:mid]
        right_branch = nums[mid+1:]

        root.left = self.sortedArrayToBST(left_branch)
        root.right = self.sortedArrayToBST(right_branch)
        return root