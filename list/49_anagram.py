#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:18:53 2020

@author: jinlingxing
"""

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs_sorted = []
for i in strs:
    m = ''.join(sorted(i))
    strs_sorted.append(m)

strs_map = list(zip(strs_sorted, strs))
res = {}
for line in strs_map:
    if line[0] in res:
        res[line[0]].append(line[1])
    else:
        res[line[0]] = [line[1]]
res.values()


    




        