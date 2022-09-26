#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:28:31 2020

@author: jinlingxing
"""

# from collections import Counter
# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         n = Counter(name)
#         sorted_n = sorted(n.items(), key=lambda x: x[1], reverse = True)
#         t = Counter(typed)
#         sorted_t = sorted(t.items(), key=lambda x: x[1], reverse = True)
#         count = 0
#         if len(sorted_n) > len(sorted_t):
#             return False
#         for i in range(len(sorted_n)):
#             for j in range(len(sorted_t)):
#                 if sorted_n[i][0] == sorted_t[j][0]:
#                     if sorted_n[i][1]<=sorted_t[j][1]:
#                         count += 1
#                     else:
#                         return False
#         return count!=0
  


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False
        if len(name) == len(typed):
            return True
        i=0
        j=0
        while j<len(typed):
            if i<len(name) and name[i]==typed[j]:
                i+=1
            elif j==0 or typed[j]!=typed[j-1]: #if it's long pressed
                return False
            j+=1
        return i==len(name)
        
sol = Solution()
name = "kikcxmvzi"
typed = "kiikcxxmmvvzz"
sol.isLongPressedName(name, typed)
