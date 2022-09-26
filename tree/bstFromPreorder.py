#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:25:04 2020

@author: jinlingxing
"""

'''
Problem: Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
 any descendant of node.left has a value < node.val, 
 and any descendant of node.right has a value > node.val. 
 Also recall that a preorder traversal displays the value of the node first,
 then traverses node.left, then traverses node.right.)


Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        def helper(preorder, limit):
            #need to pop the first element of preorder, 
            #so we need to make sure the preorder[0] is in the bound
            if preorder and preorder[0] < limit: 
                val = preorder.pop(0)
                root = TreeNode(val)
                root.left = helper(preorder, val)
                root.right = helper(preorder, limit)
                return root
            return None
            
        res = helper(preorder, float('inf'))
        return res
        
if __name__ == "__main__":
    preorder = [8,5,1,7,10,12]
    #root = 8, root.left is [5,1,7], root.right is [10,12]
    sol = Solution()
    sol.bstFromPreorder(preorder)