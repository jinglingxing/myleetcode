#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:34:51 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem:
    Given a binary tree, you need to compute the length of the diameter of 
    the tree. The diameter of a binary tree is the length of the longest 
    path between any two nodes in a tree. This path may or may not pass 
    through the root. 

Example :
    Given a binary tree 
          1
         / \ 
        2   3
       / \     
      4   5 

     Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: 
    The length of path between two nodes is represented by the number
    of edges between them. 
'''


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # returns max_depth and max diameter
        def dfs(node) -> (int, int):
            if not node:
                return (0, 0)

            depth_left, diameter_left = dfs(node.left)
            depth_right, diameter_right = dfs(node.right)

            return max(depth_left, depth_right) + 1, max(depth_left + depth_right, diameter_left, diameter_right)

        return dfs(root)[1]
