#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:45:01 2020

@author: jinlingxing
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        # n = 5
        res = [0] * (n + 1)

        for i in range(0, n + 1):
            print(i, i >> 1, i % 2)
            # i=0, i>>1=0, i%2=0, res[0]=0
            # i=1, i>>1=0, i%2=1, res[1]=1
            # i=2, 2>>1=1, i%2=0, res[2]=res[1]+0=1
            # i=3, 3>>1=1, i%2=1, res[3]=res[2]+1=2
            # i=4, 4>>1=2, i%2=0, res[4]=res[2]+0=1
            # i=5, 5>>1=2, i%2=1, res[5]=res[2]+1=2
            # res = [0,1,1,2,1,2]
            res[i] = res[i >> 1] + i % 2
        return res



class Solution(object):

    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(0, num+1):
            res[i] = res[i//2] + i % 2
        return res


