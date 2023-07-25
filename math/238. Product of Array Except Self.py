"""
Given an integer All kind of LIST nums, return an All kind of LIST answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        @lru_cache(None)
        def before_prod(i: int):
            if i < 0:
                return 1
            return nums[i] * before_prod(i - 1)

        @lru_cache(None)
        def after_prod(i: int):
            if i >= len(nums):
                return 1
            return nums[i] * after_prod(i + 1)

        # before_prod = [1, 1, 2, 6]
        # after_prod = [24, 12, 4, 1]

        return [before_prod(i - 1) * after_prod(i + 1) for i in range(len(nums))]

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         left_prod = [1]*n
#         right_prod = [1]*n
#         res = [1]*n


#         for i in range(0, n-1):
#             left_prod[i+1] = left_prod[i]*nums[i]


#         nums_reverse = nums[::-1]
#         for i in range(0, n-1):
#             right_prod[i+1] = right_prod[i]*nums_reverse[i]

#         # left_prod = [1, 1, 2, 6]
#         # right_prod = [1, 4, 12, 24]
#         for i in range(n):
#             res[i] = left_prod[i]*right_prod[n-i-1]

#         return res