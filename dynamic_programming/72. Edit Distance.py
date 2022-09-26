#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:43:36 2020

@author: jinlingxing
"""
'''
Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#          dp = [[0 for x in range(len(words2)+1] for y in range(len(words1)+1)]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)+1
        n = len(word1)+1
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = i
        for j in range(m):
            dp[0][j] = j
        for i in range(1,n):
            for j in range(1,m):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j] -> insert
                    # dp[i][j-1] -> remove
                    # dp[i-1][j-1] -> replace
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]
            
    #     r o s
    #   0 1 2 3
    # h 1 1 2 3
    # o 2 2 1 2 
    # r 3 2 2 2
    # s 4 3 3 2
    # e 5 4 4 3
    
sol = Solution()
word1 = 'horse'
word2 = 'ros'
sol.minDistance(word1, word2)

    
    
    
    
    