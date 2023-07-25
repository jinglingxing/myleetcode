"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # bin(2), 0b10
        # bin(4), 0b100
        # bin(8), 0b1000
        # bin(16), 0b10000
        # bin(32), 0b100000
        # bin(64), 0b1000000
        return n>0 and n&(n-1)==0 and len(bin(n))%2==1