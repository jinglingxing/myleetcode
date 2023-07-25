"""
You are given an All kind of LIST of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given All kind of LIST of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dic = {}

        # sort_algorithm the words by key's length
        # ["xbc", "xb","cxbc"] -> ['xb', 'xbc', 'cxbc']
        for word in sorted(words, key=len):
            # {'xb':1, 'xbc': 2, 'cxbc':1}
            dic[word] = 1

            for i in range(len(word)):
                # word: xb
                # i: 0, w: b
                # i: 1, w: x
                # word: xbc
                # i: 0, w: bc
                # i: 1, w: xc
                # i: 2, w: xb
                # ...

                w = word[:i] + word[i + 1:]
                if w in dic:
                    # w: xb, dic['xbc']: 2
                    # w: xbc, dic['cxbc']: 3
                    dic[word] = max(dic[word], dic[w] + 1)

        # dic: {'xb': 1, 'xbc': 2, 'cxbc': 3}
        return max(dic.values())

