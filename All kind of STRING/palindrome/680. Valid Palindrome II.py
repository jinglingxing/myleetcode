class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Time limit exceeded
        # for i in range(len(s)):
        #     deleted_s = s[:i]+s[i+1:]
        #     if deleted_s == deleted_s[::-1]:
        #         return True
        # return False

        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return s[left:right]==s[left:right][::-1] or s[left+1:right+1]==s[left+1:right+1][::-1]
            left += 1
            right -= 1

        return True