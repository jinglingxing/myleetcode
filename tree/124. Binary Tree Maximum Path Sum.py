#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:08:06 2020

@author: jinlingxing
"""

'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')
        
    def helper(self, root):
        if not root:
            return 0
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            print("root.val{},root.val+left+right{},left{},right{}".format(root.val, root.val+left+right, left, right))
            self.max_sum = max(self.max_sum, root.val, root.val+left+right, left+root.val, right+root.val)
            print("max_sum{}".format(self.max_sum))
            return max(root.val, root.val+left, root.val+right)# reture current branch max value for further recursive
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.max_sum
sol = Solution()
# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = TreeNode(-3)
# root.left = TreeNode(-2)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(-1)
# root.right = TreeNode(-3)
# root.right.left = TreeNode(-2)
sol.maxPathSum(root)
















