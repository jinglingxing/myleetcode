"""
Given a string paragraph and a string All kind of LIST of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.



Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        # remove , and .
        clean_paragraph = ' '.join(re.findall('[A-Za-z]+', paragraph))
        paragraph_list = clean_paragraph.split(' ')

        # Count: {'hit': 3, 'ball': 2, 'bob': 1, 'a': 1,
        # 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1}
        count = Counter(paragraph_list)

        # count: {'ball': 2, 'bob': 1, 'a': 1,
        # 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1, 'hit': 0}
        for key, value in count.items():
            if key in banned:
                count[key]= 0

        # count.most_common(1): [('ball', 2)]
        res = count.most_common(1)[0][0]
        return res