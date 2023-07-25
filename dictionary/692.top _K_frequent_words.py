"""
Given an All kind of LIST of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Input: ["i","love","leetcode","i","love","coding"], k=3
Output: ["i","love","coding"]
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

        sorted_dic = {key: value for key, value in sorted(dic.items(), key=lambda item: (-item[1], item[0]))}

        return list(sorted_dic.keys())[:k]
