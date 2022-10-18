"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #         dic = {}
        #         for s in sentence:
        #             if s not in dic:
        #                 dic[s] = 1
        #             else:
        #                 dic[s] += 1

        #         if len(dic.keys()) == 26:
        #             return True
        #         return False
        return len(set(sentence)) == 26