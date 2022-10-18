"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # 1: 1
        # 2: 11
        # 3: 21
        # 4: 1211
        # 5: 111221
        # 6: 312211
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)

        res = ""
        count = 1
        for i in range(len(prev)):
            # 1211
            if i == len(prev) - 1 or prev[i] != prev[i + 1]:
                res += str(count) + prev[i]
                count = 1
            # 111221
            else:
                count += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 4
    sol.countAndSay(4)