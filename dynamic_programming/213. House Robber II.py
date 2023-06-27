#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:39:35 2020

@author: jinlingxing
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        nums1 = nums[:-1]
        nums2 = nums[1:]

        dp1 = [0] * len(nums1)
        dp2 = [0] * len(nums2)

        dp1[0], dp1[1] = nums1[0], max(nums1[1], nums1[0])
        dp2[0], dp2[1] = nums2[0], max(nums2[1], nums2[0])

        for i in range(2, len(nums1)):
            dp1[i] = max(max(dp1), dp1[i - 2] + nums1[i])
            dp2[i] = max(max(dp2), dp2[i - 2] + nums2[i])

        return max(dp1[-1], dp2[-1])


if __name__ == "__main__":
    sol = Solution()
#    nums = [1,3,1,3,100]
    nums = [2,7,9,3,1]
    sol.rob(nums)