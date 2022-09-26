#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:56:54 2020

@author: jinlingxing
"""
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a_pointer = 0
        b_pointer = -1
#        s = re.sub('[^a-zA-Z]' or '[^0-9]', '', s)
        s = re.sub('[^\w]', '', s)
        s = s.lower()
        if(len(s) == 0 or len(s) == 1):
            return True

        if(len(s) > 1):  
            while(a_pointer <= len(s)/2):
                if(s[a_pointer] == s[b_pointer]):
                    a_pointer += 1
                    b_pointer -= 1
                else:
                    return False
            return True
                
            

        
if __name__ == "__main__":
    sol = Solution()
    s = "9 #ab@ a 9"
    sol.isPalindrome(s)