"""
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.



Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
Example 2:

Input: order = "cbafg", s = "abcd"
Output: "cbad"
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # order = "cba", s = "abcd"
        # Count the occurrence of each char in s
        dic_s = Counter(s)

        # build the string  in order
        res = ''
        for char in order:
            # char = 'c', dic_s = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})
            # char = 'b', dic_s = Counter({'a': 1, 'b': 1, 'd': 1})
            # char = 'a', dic_s = Counter({'a': 1, 'd': 1})
            # dic_s = Counter({'d': 1})
            if char in dic_s:
                # res: 'cba'
                res += char * dic_s[char]
                # remove the used char
                dic_s.pop(char)

        # res: 'cbad'
        for char, val in dic_s.items():
            res += char * val

        return res