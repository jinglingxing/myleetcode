#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:40:51 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #define a function dfs
        def dfs(i, adjacency, flags):
            #if flag[i] = -1, node i has been visted, return true
            #if flag[i] = 1, node i have been visted twice, there is a cycle, return false
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            #set flag[i] = 1, it means it has been visted in this loop
            flags[i] = 1
            #iterate all the adjacency node of node i, if it has a loop, return false
            for j in adjacency[i]:
                if not dfs(j,adjacency,flags): 
                    return False
            #when we vistied all the adjacency nodes of node i, set flag[i]=-1 and return true
            flags[i] = -1
            return True
        #adjacency = [[]]*numCourses #[[],[]]
        #flags = [0]*numCourses#[0,0]
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): 
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    numCourses = 2
    pre = [[1,0]]
    sol.canFinish(numCourses, pre)