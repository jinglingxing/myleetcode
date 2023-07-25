#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 12:07:33 2020

@author: jinlingxing
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = bin(int(a,2) + int(b,2))
        return c[2:]