"""
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.



Example 1:

Input: "112358"
Output: true
Explanation:
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        # note 1 : the hardest part is to find the two first number (are they always ordered? -> no, current solution doesn't work)
        # note 2 : knowing the sum of the two numbers, we can guess the length of the next number (in terms of digits)

        def f(i: int, j: int):
            p00 = 0
            p01 = p10 = i
            p11 = j

            while True:
                num1 = int(num[p00:p01])
                num2 = int(num[p10:p11])

                if num[p00:p01][0] == "0" and num1 or num[p10:p11][0] == "0" and num2:
                    return False
                s = num1 + num2
                l = len(str(s))
                if len(num) - p11 - l < 0:  # we are over the end of the string
                    return False

                num3 = int(num[p11:p11 + l])

                if num3 != s:
                    return False

                p00, p01 = p10, p11
                p10, p11 = p11, p11 + l

                if p11 == len(num):
                    return True

        if len(num) < 3:
            return False

        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                if f(i, j):
                    return True

        return False
