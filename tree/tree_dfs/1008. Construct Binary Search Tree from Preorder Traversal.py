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
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def dfs(preorder: List[int]):
            if not preorder:
                return None

            val = preorder.pop(0)
            node = TreeNode(val)

            left_preorder = []
            right_preorder = []
            for n in preorder:
                if n < val:
                    left_preorder.append(n)
                else:
                    right_preorder.append(n)

            node.left = dfs(left_preorder)
            node.right = dfs(right_preorder)

            return node

        return dfs(preorder)