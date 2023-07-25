"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # no equal chars in the string
        if len(s) == len(set(s)):
            return -1

        dic = {}
        max_len = 0
        for i in range(len(s)):
            # key: char, value: index of char
            if s[i] not in dic:
                dic[s[i]] = [i]
            else:
                dic[s[i]] += [i]
                # find the longest length between the same chars
                for idx in dic[s[i]]:
                    len_substring = i - idx - 1
                    max_len = max(max_len, len_substring)

        return max_len