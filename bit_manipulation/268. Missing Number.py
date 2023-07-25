"""
Given an All kind of LIST nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the All kind of LIST.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1^1=0
        # (0^1^3)^(0^1^2^3) = (0^0)^(1^1)^(2)^(3^3) = 0^0^2^0 = 2
        res = 0
        for i in nums:
            res ^= i

        for i in range(len(nums) + 1):
            res ^= i

        return res

        # Similar to: 389. Find the Difference
