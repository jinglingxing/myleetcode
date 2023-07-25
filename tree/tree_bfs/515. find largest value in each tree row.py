#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:47:57 2020

@author: jinlingxing
"""

'''
Given the root of a binary tree, return an list of the largest value in each row of the tree (0-indexed).

 

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
'''

from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = [root]
        res = []

        while q:
            level = len(q)
            level_list = []
            while level:
                node = q.pop(0)
                level_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level -= 1
            res.append(max(level_list))
        return res
        
    
sol = Solution() 
root = TreeNode(1)
root.left = (TreeNode(3))
root.left.left = (TreeNode(5))
root.left.right = (TreeNode(3))
root.right = (TreeNode(2))
root.right.right = (TreeNode(9))
sol.largestValues(root)
print(sol.largestValues(root))




