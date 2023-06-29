class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        odd_count = 0
        sum_freq = 0
        for i, key in enumerate(dic):
            val = dic[key]
            sum_freq += val
            if val%2==1:
                odd_count += 1

        return sum_freq-odd_count+1 if odd_count!=0 else sum_freq-odd_count
