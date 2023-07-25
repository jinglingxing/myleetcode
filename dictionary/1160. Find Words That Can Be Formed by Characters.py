"""
You are given an list of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        res = 0

        # words = ["cat","bt","hat","tree"]
        #
        for word in words:
            flag = True
            # cat
            # hat
            for char in word:
                # c:1, c:1
                # a:1, a:2
                # t:1, t:1
                # h:1, h:1
                # a:1, a:2
                # t:1, t:1
                # tree, e:2, e:0, flag=False
                if word.count(char) > chars_count[char]:
                    flag = False
            # res=cathat
            if flag:
                res += len(word)

        return res