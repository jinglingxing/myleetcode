#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:08:43 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem :
    Given an array of strings, group anagrams together.

Example :
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for i in strs:
            m = "".join(sorted(i))
            sorted_strs.append(m)
        strs_map = list(zip(sorted_strs, strs))
        res = {}
        for line in strs_map:
            if line[0] in res:
                res[line[0]].append(line[1])
            else:
                res[line[0]] = [line[1]]
        return res.values()

if __name__=='__main__':
    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    out = sol.groupAnagrams(inp)
    print("The solution to {} is : {}".format(inp, out))
