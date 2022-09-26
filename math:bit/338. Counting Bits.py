#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:45:01 2020

@author: jinlingxing
"""
class Solution(object):

    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(0,num+1):
            res[i]= res[i//2] + i%2
        return res


if __name__ == "__main__":
    sol = Solution()
    numb = 5
    print(sol.countBits2(numb))