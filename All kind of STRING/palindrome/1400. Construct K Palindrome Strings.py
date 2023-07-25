class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        for val in dic.values():
            if val % 2 == 1:
                k -= 1

            if k == -1:
                return False
        return True