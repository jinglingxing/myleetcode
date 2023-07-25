"""
Given an array of strings words and a character separator, split each string in words by separator.

Return an array of strings containing the new strings formed after the splits, excluding empty strings.

Notes

separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
A split may result in more than two strings.
The resulting strings must maintain the same order as they were initially given.


Example 1:

Input: words = ["one.two.three","four.five","six"], separator = "."
Output: ["one","two","three","four","five","six"]
Explanation: In this example we split as follows:

"one.two.three" splits into "one", "two", "three"
"four.five" splits into "four", "five"
"six" splits into "six"

Hence, the resulting array is ["one","two","three","four","five","six"].

"""


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for str_ in words:
            new_str = list(str_.split(separator))
            res += new_str
        res = [x for x in res if x]
        return res