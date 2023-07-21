"""
Given a string s, return the maximum number of occurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.


Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
"""


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # s = "aababcaab"
        n = len(s)
        dic = defaultdict(int)
        # maxSize doesn't matter
        for i in range(n - minSize + 1):
            # i=0, j=3, sub: aab
            # i=1, j=4, sub: aba
            # i=2, j=5, sub: bab
            # i=3, j=6, sub: abc
            # i=4, j=7, sub: bca
            # i=5, j=8, sub: caa
            # i=6, j=9, sub: aab
            j = i + minSize
            sub = s[i:j]
            # {'aab': 1, 'aba':2, 'bab':1, 'cca':1}

            if len(set(sub)) <= maxLetters:
                dic[sub] += 1

        return max(dic.values()) if dic.values() else 0

