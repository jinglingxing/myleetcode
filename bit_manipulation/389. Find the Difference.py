"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.



Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # ord('a'): 97
        # ord('A'): 65
        # ord('A')^ord('A'): 0

        res = 0
        for i in range(len(s)):
            res ^= ord(s[i])

        for i in range(len(t)):
            res ^= ord(t[i])

        return chr(res)

        # Similar to: 268. Missing Number
