class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1

        if 'a' in s and 'b' in s:
            return 2

        return 1