"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = {}
        dp[1] = ["()"]
        dp[2] = ["(())", "()()"]

        # n = 3
        for i in range(3, n + 1):
            d = {}
            arr = []
            for st in dp[i - 1]:
                # dp[2] = ["(())","()()"]
                for j in range(0, len(st)):
                    # st (()), j=0, ()(())
                    # st (()), j=1, (()())
                    # st (()), j=2, ((()))
                    # st (()), j=3, (()())
                    # st ()(), j=0, ()()()
                    # st ()(), j=1, (())()
                    # st ()(), j=2, ()()()
                    # st ()(), j=3, ()(())
                    new = st[0:j] + "()" + st[j:len(st)]

                    # d: {()(()): 1, (()()): 1, ((())): 1, ()()(): 1, (())(): 1}
                    if new not in d:
                        d[new] = 1
                        arr.append(new)

            # dp[3] = ["((()))","(()())","(())()","()(())","()()()"]
            dp[i] = arr

        return dp[n]

