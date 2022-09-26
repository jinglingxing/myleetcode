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
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Our definition of a Tree
class Tree (object) :
    def __init__(self, inp_l: List[int] = []):
        if inp_l:
            inp = inp_l.copy()
            self.top = TreeNode(inp.pop(0))
            if inp :
                self.add_level([self.top],inp)
    
    def add_level(self, prev_lvl: List[TreeNode], inp_l: List[int]):
        lvl = []
        for prevN in prev_lvl:
            if inp_l :
                if len(inp_l) == 1:
                    value = inp_l.pop(0)
                    if value:
                        prevN.left = TreeNode(value)
                        lvl.append(prevN.left)
                elif len(inp_l) > 1:
                    value = inp_l.pop(0)
                    if value:
                        prevN.left = TreeNode(value)
                        lvl.append(prevN.left)
                    value = inp_l.pop(0)
                    if value:
                        prevN.right = TreeNode(value)
                        lvl.append(prevN.right)
        
        if inp_l:
            self.add_level(lvl, inp_l)

    def str_lvl (self, prev_lvl: List[TreeNode], prev_node_pos: List[int] = [0]) -> str:
        line1 = ''
        line2 = ''
        lvl = []
        pos = []
        for i in range (len(prev_lvl)):
            prevN = prev_lvl[i]
            posN = prev_node_pos[i]
            
            # We check if we have the right spacing based on the position
            # of the previous node
            if len(line1) != 7*posN :
                line1 += ' '*7*(posN - (len(line1)%7))
                line2 += ' '*7*(posN - (len(line2)%7))

            if prevN.left:
                line1 += ' / '
                line2 += '{} '.format(prevN.left.val)
                lvl.append(prevN.left)
                pos.append(posN*2)
            else:
                line1 += '   '
                line2 += '   '
            if prevN.right:
                line1 += ' \\ '
                line2 += '   {}'.format(prevN.right.val)
                lvl.append(prevN.right)
                pos.append(posN*2 + 1)
            else:
                line1 += '   '
                line2 += '   '
        if lvl :
            return [line1 + '\n' + line2] + self.str_lvl(lvl, pos)
        return [line1 + '\n' + line2]

    def __str__ (self) -> str:
        l_str_lvl = [str(self.top.val)]
        l_str_lvl += self.str_lvl([self.top])
        l_str_lvl.pop() #remove last element
        length_l = len(l_str_lvl)
        l_str_lvl[0] = ' '*int(7*(length_l-1)*0.5)+l_str_lvl[0]
        for i in range (1, length_l):
            #l_str_lvl[i] = ' '*7*int((length_l-i)/2) + l_str_lvl[i]
            line1 = l_str_lvl[i].split('\n')[0]
            line2 = l_str_lvl[i].split('\n')[1]
            line1 = ' '*int(7*(length_l-1-i)*0.5) + line1
            line2 = ' '*int(7*(length_l-1-i)*0.5) + line2
            l_str_lvl[i] = line1 + '\n' + line2
        return '\n'.join(l_str_lvl)


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            #calculate height of left and right subtrees
            h_left = self.height(root.left)
            h_right = self.height(root.right)
            # calculate the longest path without considering the root
            d_left = self.diameterOfBinaryTree(root.left)
            d_right = self.diameterOfBinaryTree(root.right)
            #no. edges = no.nodes - 1
            return max(h_left+h_right, max(d_left,d_right))
        
    def height(self, root):
        if root is None:
            return 0
        else:
            left = self.height(root.left)    
            right = self.height(root.right)
            return max(left,right)+1
        
        
if __name__ == "__main__":
    inp = [1,2,3,4,5, None,6]
    T = Tree(inp_l = inp)
    tnode = TreeNode(1)
    tnode.left = TreeNode(2)
    tnode.right = TreeNode(3)
    tnode.left.left = TreeNode(4)
    tnode.left.right = TreeNode(5)
    sol = Solution()
    out = sol.diameterOfBinaryTree(T.top)
    print("The solution to {} is : {}".format(inp, out))
    print('{}'.format(T))
    #print(T.str_lvl([T.top]))