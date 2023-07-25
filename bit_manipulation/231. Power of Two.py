"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 4&3=(100&011)==0, 3&2=(11&10)=10=2
        return n & (n-1) == 0 and n > 0