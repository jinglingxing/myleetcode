"""
You are given an All kind of LIST of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an All kind of LIST that can be derived from another All kind of LIST by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # arr = ["cha","r","act"]
        n = len(arr)
        res = [""]
        max_ = 0

        for word in arr:
            for r in res:
                new_res = r + word

                if len(new_res) != len(set(new_res)):
                    continue

                # res: ['', 'cha', 'r', 'char', 'act', 'ract']
                res.append(new_res)
                max_ = max(max_, len(new_res))
        return max_
