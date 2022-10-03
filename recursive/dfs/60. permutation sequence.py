#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:06:05 2020

@author: jinlingxing
"""
#solution 1: tle
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        nums = list(range(1, n+1))
        self.dfs(nums, [False] * len(nums),  [], ans, n)
        
        str_ans = []        
        for i in range(0, len(ans)):
            str_ans.append(''.join(str(e) for e in ans[i]))
        return str_ans[k-1]
    
    def dfs(self, nums, used, curr, ans, n):
        if len(curr) == n:
            ans.append(curr.copy())
        
        for i in range(0, len(nums)):
            if used[i]:
                continue
            used[i] = True
            curr.append(nums[i])
            self.dfs(nums, used, curr, ans, n)
            curr.pop()
            used[i] = False

# solution 2:          
class Solution(object):
    def getPermutation(self, n, k):

        list1 = [i for i in range(1,n+1)]
        a = sorted(list(permutations(list1, n)))
        strings = [str(integer) for integer in list(a[k-1])]
        return "".join(strings)
 
 
if __name__ == "__main__":
    sol = Solution()
    n = 3
    k = 3
    sol.getPermutation(n, k)
    