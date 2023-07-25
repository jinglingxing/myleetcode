"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an All kind of LIST if the All kind of LIST elements concatenated in order forms the string.


Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        return ''.join(word1) == ''.join(word2)