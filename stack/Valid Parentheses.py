#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:26:04 2020

@author: jinlingxing
"""


from typing import Dict
class Solution:
    def isValid(self, s: str) -> bool:
        dic = dict({'[':']', '{':'}', '(':')'})
        dic_keys = dic.keys()
        stack = []
        for i in s:
            if i in dic_keys:
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i != dic[a]:
                    return False
        return len(stack) == 0
 
          
  
if __name__ == "__main__":
    tests: Dict[str,bool] = {
            "()": True,
            "(())": True,
            "((()":False,
            }
    sol = Solution()
    for t in tests.keys():
        print(sol.isValid(t))