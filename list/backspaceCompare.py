#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:26:21 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem :
    Given two strings S and T, return if they are equal 
    when both are typed into empty text editors. 
    # means a backspace character.

Example 1 :
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2 :
    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3 :
    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4 :
    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        for i in S:
            if i == '#' :
                s_idx = S.index(i)
                if s_idx == 0 :
                    S = S[1:]
                else :
                    S = S[0:s_idx-1]+S[s_idx+1:]
        for i in T:
            if i == '#' :
                t_idx = T.index(i)  
                if t_idx == 0:
                    T = T[1:]
                else:
                    T = T[0:t_idx-1]+T[t_idx+1:]
        
        if S == T:
            return True
        else:
            return False

    def backspaceCompare2(self, S: str, T: str) -> bool:
        while '#' in S:
            idx = S.find('#')
            if idx == 0:
                S = S[1:]
            else:
                S = S[:idx-1] + S[idx+1:]
         
        while '#' in T:
            idx = T.find('#')
            if idx == 0:
                T = T[1:]
            else:
                T = T[:idx-1] + T[idx+1:]
        
        if T == S :
            return True
        else:
            return False
            
if __name__ == "__main__":
    sol = Solution()
    S = "a##c"
    T = "#a#c"
    out = sol.backspaceCompare(S, T)
    print("The solution to S : {} and T : {} is : {}".format(S, T, out))