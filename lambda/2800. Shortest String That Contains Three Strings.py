"""
Given three strings a, b, and c, your task is to find a string that has the minimum length and contains all three strings as substrings.
If there are multiple such strings, return the lexicographically smallest one.

Return a string denoting the answer to the problem.

Notes

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ,
string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
A substring is a contiguous sequence of characters within a string.


Example 1:

Input: a = "abc", b = "bca", c = "aaa"
Output: "aaabca"
Explanation:  We show that "aaabca" contains all the given strings: a = ans[2...4], b = ans[3..5], c = ans[0..2].
It can be shown that the length of the resulting string would be at least 6 and "aaabca" is the lexicographically smallest one.
"""


class Solution:
    def merge(self, s1: str, s2: str) -> str:
        if s2 in s1:
            return s1

        for i in range(len(s1)):
            if s2.startswith(s1[i:]):
                return s1[:i] + s2

        return s1 + s2

    def minimumString(self, a: str, b: str, c: str) -> str:
        res = []
        for s1, s2, s3 in permutations([a, b, c]):
            res.append(self.merge(self.merge(s1, s2), s3))

        # res: ['abcaaa', 'abcaaa', 'bcabcaaa', 'bcaaabc', 'aaabca', 'aaabca']
        return (min(res, key=lambda s: (len(s), s)))