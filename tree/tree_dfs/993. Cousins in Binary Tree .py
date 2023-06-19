#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:34:48 2020

@author: jinlingxing
"""

'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
 '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = 0

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        dic = {}

        def dfs(node: Optional[TreeNode], depth: int, parent: int):
            if not node:
                return

            if node.val == x or node.val == y:
                dic[node.val] = (depth, parent)

            dfs(node.left, depth + 1, node.val)
            dfs(node.right, depth + 1, node.val)

        dfs(root, 0, -1)

        return dic[x][1] != dic[y][1] and dic[x][0] == dic[y][0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        