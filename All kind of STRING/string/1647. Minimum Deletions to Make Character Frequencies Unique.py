"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.



Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        # s = "aaabbbcc", cnt = {a:3, b:3, c:2}
        cnt = Counter(s)
        deletions = 0
        used_freqs = set()

        for char, freq in cnt.items():
            # used_freqs = (3)
            # used_freqs = (3,2)
            # used_freqs = (3,2,1)
            while freq > 0 and freq in used_freqs:
                freq -= 1
                deletions += 1
            used_freqs.add(freq)

        return deletions


