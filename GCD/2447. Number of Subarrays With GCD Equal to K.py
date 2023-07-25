"""
Given an integer list nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an list.

The greatest common divisor of an list is the largest integer that evenly divides all the list elements.



Example 1:

Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
Example 2:

Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.
"""


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


from typing import List
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            curr_gcd = 0
            for j in range(i, len(nums)):
                curr_gcd = gcd(curr_gcd, nums[j])
                res += (curr_gcd == k)

        return res


if __name__ == '__main__':
    sol = Solution()
    sol.subarrayGCD(nums=[9, 3, 1, 2, 6, 3], k=3)
