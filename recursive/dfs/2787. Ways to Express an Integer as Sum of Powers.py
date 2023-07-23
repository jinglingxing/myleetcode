class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7
        # @cache

        # depth = 1, remaining_sum = 10, base = 1, return 1+0=1
        # depth = 2, x: result = 10-1**2 = 9, base = 2, return 1
        # depth = 3, x: result = 9-2**2 = 5, base = 3, return 0
        # depth = 4, x: result = 5-3**2 = -4, return 0
        # depth = 3, y: remaining_sum = 9, result = 9-3**2 = 0, return 1
        # return 0+1
        # depth = 2, y: remaining_sum = 10, result = 10-2**2 = 6, base = 2, return 0
        # depth = 3, x: remaining_sum = 6, result = 6-3**2 = -3, base = 3, return 0
        # depth = 3, y: remaining_sum = 10, result = 10-3**3 = 1, base = 4, return 0
        # depth = 4, x: result < 0, return 0
        # depth = 4, y: result < 0, return 0

        def dfs(remaining_sum, power, base):
            result = remaining_sum - pow(base, power)

            if result == 0:
                return 1
            if result < 0:
                return 0
            if result > 0:
                x = dfs(result, power, base + 1)
                y = dfs(remaining_sum, power, base + 1)
                return x + y

        return dfs(n, x, 1) % mod


if __name__ == '__main__':
    sol = Solution()
    res= sol.numberOfWays(10, 2)
    print(res)
