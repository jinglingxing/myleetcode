#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:11:36 2020

@author: jinlingxing
"""

# Definition for a binary tree node.
#class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def maxDepth(self, root: TreeNode) -> int:
        if root is not None:
            left_max = self.maxDepth(root.left)
            right_max = self.maxDepth(root.right)
            return max(left_max, right_max)+1
        else:
            return 0
        
    
    
