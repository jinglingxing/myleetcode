#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:52:33 2021

@author: jinlingxing
"""
from typing import List
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        out = []
        q = [root]
        while q:
            level = len(q)
            ans = []
            while level:
                node = q.pop(0)
                level -=1
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(ans)
        return out  
    
    

       
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.left.left = None
root.right.left.right = None
root.right.right.left = None
root.right.right.right = None


sol = Solution()
sol.levelOrder(root)