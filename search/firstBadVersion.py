#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:59:17 2020

@author: jinlingxing
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left<=right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left #or return right+1