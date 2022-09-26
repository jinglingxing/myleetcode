#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:14:49 2020

@author: jinlingxing
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        if len(s) == 0:
            return 0
        S = set()
        a_pointer = 0
        b_pointer = 0
        longest = 0
        i = 0
        while(b_pointer < len(s)):
            if(s[b_pointer] not in S):
                S.add(s[b_pointer])
                print(S)
                b_pointer += 1
                longest = max(len(S),longest)
            else:
                S.remove(s[a_pointer])
                print(S)
                a_pointer += 1
            i+=1
        return longest
                
                    
if __name__ == "__main__":
    sol = Solution()    
    s = "pwwkew"
    sol.lengthOfLongestSubstring(s)                