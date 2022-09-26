#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:08:38 2020

@author: jinlingxing
"""
class Solution(object):
    def findComplement(self, num: int) -> int:
        complement = 0
        digit = 0
        while num > 0:
            if num % 2 == 0:
                #complement += 2 ** digit
                complement += (1<<digit)
            digit += 1
            num >>= 1
        return complement

sol = Solution()
num = 5
sol.findComplement(num)