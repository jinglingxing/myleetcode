#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:02:19 2020

@author: jinlingxing
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: #root is empty
            return True 
        t1 = root.left
        t2 = root.right
        return self.isMirror(t1, t2)
        
    def isMirror(self, t1: TreeNode, t2: TreeNode):
        if t1==None and t2==None:
            return True
        if t1==None or t2==None:
            return False
        if t1.val == t2.val:
            if self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right):
                return True
        else:
            return False