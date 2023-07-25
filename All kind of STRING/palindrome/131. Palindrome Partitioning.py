class Solution:
    @lru_cache
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]

        ans = []
        for i in range(1, len(s) + 1):
            pref = s[:i]
            if pref == pref[::-1]:
                suff = s[i:]
                for j in self.partition(suff):
                    ans.append([s[:i]] + j)

        return ans


