"""
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.



Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
"""


class Solution:
    def beautySum(self, s: str) -> int:
        # s = "aabcb"
        n = len(s)
        beauty = 0

        for i in range(n - 1):
            dic = defaultdict(int)
            for j in range(i, n):
                dic[s[j]] += 1
                # i=0, j=2, aab: {'a':2, 'b':1}, beauty=1
                # i=0, j=3, aabc: {'a':2, 'b':1, 'c':1}, beauty=2
                # i=0, j=2, aabcb: {'a':2, 'b':2, 'c':1}, beauty=3
                # i=1, j=1, a: {'a':1}, beauty=3
                # i=1, j=2, ab: {'a':1, 'b':1}, beauty=3
                # i=1, j=3, abc
                # i=1, j=4, abcb: beauty=4
                # ...
                beauty += max(dic.values()) - min(dic.values())
                print(i, j, s[j], dic, beauty)

        return beauty
