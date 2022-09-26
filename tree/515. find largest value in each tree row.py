#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:47:57 2020

@author: jinlingxing
"""

'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

 

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
    def __init__(self):
        self.res = []
        
    #leetcode 102    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        q = deque([root])
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            self.res.append(temp)
    
    
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        self.levelOrder(root)
        for i in range(0, len(self.res)):
            ans.append(max(self.res[i]))
        return ans
        
    
sol = Solution() 
root = TreeNode(1)
root.left = (TreeNode(3))
root.left.left = (TreeNode(5))
root.left.right = (TreeNode(3))
root.right = (TreeNode(2))
root.right.right = (TreeNode(9))
sol.largestValues(root)
print(sol.largestValues(root))




