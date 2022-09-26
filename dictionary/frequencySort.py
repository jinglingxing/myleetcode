#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:24:50 2020

@author: jinlingxing
"""

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
#solution 1:

# class Solution:
#     def frequencySort(self, s: str) -> str:
#         dic = {}
#         for i in s:
#             if i in dic:
#                 dic[i] += 1
#             else:
#                 dic[i] = 1
#         dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)

#         res = ''
#         for i in range(0,len(dic_list)):
#             count = dic_list[i][1]
#             while count>0:
#                 res += dic_list[i][0]
#                 count -= 1
#         return res
  
#solution 2:

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
#         dic = {}
#         for i in s:
#             if i in dic:
#                 dic[i] += 1
#             else:
#                 dic[i] = 1
        
        dic = dict(Counter(s))
        
        dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        res = ''
        for items in dic_list:
            res += str(items[0] * items[1])
            
        # for i in range(0,len(dic_list)):
        #     count = dic_list[i][1]
        #     while count>0:
        #         res += dic_list[i][0]
        #         count -= 1
        return res    

sol = Solution()
s = 'tree'
sol.frequencySort(s)










