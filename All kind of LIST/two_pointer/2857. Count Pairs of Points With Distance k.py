"""
You are given a 0-indexed sorted array of integers nums.

You can perform the following operation any number of times:

Choose two indices, i and j, where i < j, such that nums[i] < nums[j].
Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
Return an integer that denotes the minimum length of nums after performing the operation any number of times (including zero).

Note that nums is sorted in non-decreasing order.



Example 1:

Input: nums = [1,3,4,9]
Output: 0
Explanation: Initially, nums = [1, 3, 4, 9].
In the first operation, we can choose index 0 and 1 because nums[0] < nums[1] <=> 1 < 3.
Remove indices 0 and 1, and nums becomes [4, 9].
For the next operation, we can choose index 0 and 1 because nums[0] < nums[1] <=> 4 < 9.
Remove indices 0 and 1, and nums becomes an empty array [].
Hence, the minimum length achievable is 0.
"""


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:

        # [1,3,3,3,4], output=1
        length = len(nums)
        ans = len(nums)

        i = 0
        j = (length + 1) // 2  # 3

        while i < length // 2 and j < length:
            if nums[i] < nums[j]:
                ans -= 2
            i += 1
            j += 1

        return ans

# Wrong answer
#         while nums:
#             l, r = 0, len(nums)-1
#             if l == r or nums[l] == nums[r]:
#                 return len(nums)

#             if nums[l] < nums[r]:
#                 nums.pop(0)
#                 nums.pop(-1)


#         return 0


