#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:22:33 2020

@author: jinlingxing
"""



'''
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

    Hide Hint #1  
Will Brute force work here? Try to optimize it.

   Hide Hint #2  
Can we optimize it by using some extra space?

   Hide Hint #3  
What about storing sum frequencies in a hash table? Will it be useful?

   Hide Hint #4  
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
'''

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #need to make sure sum_array[0]=0, in case the sum[0] is not zero
        pre_sum = [0]*(len(nums)+1)
        count = 0
        #sum_array is set to be zero defaultly, we start from 1 to iterate nums
        for i in range(1,len(nums)+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
        #make sure j > i and iterate on sum_array
        # this method is correct, but it is slow
        # for i in range(0, len(sum_array)-1):
        #     for j in range(i+1, len(sum_array)):
        #         if (sum_array[j] - sum_array[i] == k):
        #             count+=1
        dic = {}
        for i in range(0, len(pre_sum)):
            if pre_sum[i] - k in dic:
                count+=dic[pre_sum[i]-k]
            dic[pre_sum[i]] = dic.get(pre_sum[i], 0) + 1
        return count
sol = Solution()
nums = [1,2,0,1,2,1]
k = 4
sol.subarraySum(nums,k)
