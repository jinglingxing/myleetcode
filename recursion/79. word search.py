#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:23:44 2020

@author: jinlingxing
"""

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = len(board)
        y = len(board[0])
        
        for i in range(0, x):
            for j in range(0,y):
                if self.search(i,j,0,board, word):
                    return True
        return False
    def search(self, x,y,d, board, word):
        #if out of bound, return false
        if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
            return False
        #if word is not in board, return false
        if word[d] != board[x][y]:
            return False
        #if reached the last letter of word, return true
        if d == len(word)-1:
            return True
        #search neighbours
        curr = board[x][y]
        board[x][y] = 0
        find = self.search(x-1, y, d+1, board, word) or \
                self.search(x, y-1, d+1, board, word) or \
                self.search(x+1, y, d+1, board, word) or \
                self.search(x, y+1, d+1, board, word)
        board[x][y] = curr
        return find

sol = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"
sol.exist(board, word)

