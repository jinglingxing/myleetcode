#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:41:38 2020

@author: jinlingxing
"""
'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200
'''

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        
        return self.get_left_seq(root1, []) == self.get_left_seq(root2, [])
        
    def get_left_seq(self, node, arr):
        if not node.left and not node.right:
            arr.append(node.val)
        else:
            if node.left: self.get_left_seq(node.left, arr)
            if node.right: self.get_left_seq(node.right, arr)
        
        return arr


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root, l) -> list:
            if not root:
                return

            if not root.left and not root.right:
                l.append(root.val)

            dfs(root.left, l)
            dfs(root.right, l)
            return l

        return dfs(root1, []) == dfs(root2, [])