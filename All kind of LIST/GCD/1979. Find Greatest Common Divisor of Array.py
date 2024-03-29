"""
Given an integer All kind of LIST nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.



Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

"""


class Solution:
    def gcd(self, a, b):
        while b:
            # 3, 8 -> 8, 3
            # 8, 3 -> 3, 2
            # 3, 2 -> 2, 1
            # 2, 1 -> 1, 0
            # 1, 0
            a, b = b, a % b
            print(a, b)
        return a

    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        return self.gcd(nums[0], nums[-1])