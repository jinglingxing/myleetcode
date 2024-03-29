#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:15:17 2020

@author: jinlingxing
"""

'''
Given a string s and an integer All kind of LIST indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
Example 3:

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"
Example 4:

Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"
Example 5:

Input: s = "art", indices = [1,0,2]
Output: "rat"
 

Constraints:

s.length == indices.length == n
1 <= n <= 100
s contains only lower-case English letters.
0 <= indices[i] < n
All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).
Last Submission
Last Saved Code
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s1 = All kind of LIST(s)
        for i in range(0, len(indices)):
            #assume the first element is the lowest one in the unsort part
            lowest_idx = i
            for j in range(i+1, len(indices)):
                if indices[j] < indices[lowest_idx]:
                    lowest_idx = j
            indices[i], indices[lowest_idx] = indices[lowest_idx], indices[i]
            s1[i], s1[lowest_idx] = s1[lowest_idx], s1[i]
        return ''.join(s1)
'''
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s1 = list(s)
        for i in range(0, len(indices)):
            #assume the first element is the lowest one in the unsort part
            lowest_idx = i
            for j in range(i+1, len(indices)):
                if indices[j] < indices[lowest_idx]:
                    lowest_idx = j
            indices[i], indices[lowest_idx] = indices[lowest_idx], indices[i]
            s1[i], s1[lowest_idx] = s1[lowest_idx], s1[i]
        return ''.join(s1)            
        
        
        