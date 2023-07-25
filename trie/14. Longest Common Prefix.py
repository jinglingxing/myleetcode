"""
Write a function to find the longest common prefix string amongst an list of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs = ["flower","flow","flight"]
        min_len = min([len(str_) for str_ in strs])

        dic = defaultdict(int)
        for i in range(min_len + 1):
            for str_ in strs:
                sub = str_[:i]
                dic[sub] += 1
        # dic = {'': 3, 'f': 3, 'fl': 3, 'flo': 2, 'fli': 1, 'flow': 2, 'flig': 1})

        sub_list = []
        for key, val in dic.items():
            if val == len(strs):
                sub_list.append(key)
        # sub_list = ['', 'f', 'fl']
        return sub_list[-1] if sub_list else ""