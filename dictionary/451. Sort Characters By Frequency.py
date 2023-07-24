"""
Given a string s, sort_algo it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        # s = "tree"
        # dic = {'t': 1, 'r': 1, 'e': 2}
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1

        # sorted_dic = {'e': 2, 't': 1, 'r': 1}
        sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        # ['ee', 't', 'r']
        sorted_list = [k * v for k, v in sorted_dic.items()]
        return ''.join(sorted_list)
