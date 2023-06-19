#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:20:42 2020

@author: jinlingxing
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inorder(root)[k-1]
    
    def inorder(self, root):
        if not root:
            return []
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return left+[root.val]+right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []

        def inorder(node: Optional[TreeNode]) -> list:
            if not node:
                return
            inorder(node.left)
            l.append(node.val)
            inorder(node.right)
            return l

        return inorder(root)[k - 1]


sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
k=3
sol.kthSmallest(root, k)
