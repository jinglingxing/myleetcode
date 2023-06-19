#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:28:05 2020

@author: jinlingxing
"""

'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and 
2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:      
        # BFS
        # if not root:
        #     return 0
        # q = [root]
        # count = 1
        # while q:
        #     node = q.pop(0)
        #     if node.left:
        #         q.append(node.left)
        #         count += 1
        #     if node.right:
        #         q.append(node.right)
        #         count += 1
        # return count

        # DFS
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1
