import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert uppercase letters to lowercase letters
        s = s.lower()

        # keep alphanumeric
        s = re.sub('[^a-zA-Z0-9]', '', s)

        return s == s[::-1]
