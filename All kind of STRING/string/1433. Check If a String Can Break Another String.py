"""
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.



Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # Strings abc, xya
        # After sorted -> s1: abc, s2: axy
        s1 = sorted(s1)
        s2 = sorted(s2)

        count1, count2 = 0, 0
        for i in range(len(s1)):
            # ord(a) -> 97
            # count1: 1
            # count2: 3
            if ord(s1[i]) >= ord(s2[i]):
                count1 += 1
            if ord(s2[i]) >= ord(s1[i]):
                count2 += 1

        if count1 == len(s1) or count2 == len(s2):
            return True
        else:
            return False