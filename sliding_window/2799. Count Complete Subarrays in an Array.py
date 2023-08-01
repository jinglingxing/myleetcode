"""
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.



Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

"""


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # nums = [1,3,1,2,2], total_distinct = 3
        # i=0, j=0, cur=[1], j=1, cur=[1,3], j=2, cur=[1,3], j=3, cur=[1,3,2], res=1
        ans = 0
        total_distinct = len(set(nums))
        for i in range(len(nums)):
            cur = set()
            for j in range(i, len(nums)):
                cur.add(nums[j])
                if len(cur) > total_distinct:
                    break
                if len(cur) == total_distinct:
                    ans += 1
        return ans
        # d = len(set(nums))
        # n = len(nums)
        # count = 0
        # s = set()

        # for i in range(n-d+1):
        #     j = i+d-1
        #     while j < n:
        #         sub = nums[i:j+1]
        #         j += 1
        #         if len(set(sub)) == d:
        #             count += 1
        # return count


