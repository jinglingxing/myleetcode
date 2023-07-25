#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:55:55 2020

@author: jinlingxing
"""

'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
Example 4:

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""
 

Constraints:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #assume len(str1) >= len(str2)
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        #m>=n
        m = len(str1)
        n = len(str2)
        i = n
        while i > 0:
            if m%i==0 and n%i==0:
                if str2[0:i]*(n//i)==str2 and str2[0:i]*(m//i) == str1:
                    return str2[0:i]
            i-=1
        return ''
                
# str1 = "ABCDEF", str2 = "ABC", the following result will return 'ABC' rather than ''
#        dic1 = {}
#        dic2 = {}
        #str1 = "ABABAB", dic1 = {1: 'A', 2: 'AB', 3: 'ABC', 4: 'ABCA', 5: 'ABCAB', 6: 'ABCABC'}
#        for i in range(0, len(str1)):
#            dic1[i+1] = str1[0:i+1]
#        for i in range(0, len(str2)):
#            dic2[i+1] = str2[0:i+1]
        
#        for i in range(1, len(dic2)+1):
#            if len(str1) % i == 0 and len(str1) // i != len(str1) and len(str2) % i == 0 and len(str2) // i != len(str2) and dic1[i] == dic2[i]:
#                return dic1[i]
#        return ''