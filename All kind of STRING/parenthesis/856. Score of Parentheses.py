class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        flag = 0
        stack = []

        for char in s:
            if char == '(':
                flag = 1
                stack.append('(')
            if char == ')':
                if flag == 1:
                    score += 2**(len(stack)-1)
                    flag = 0
                stack.pop(0)
        return score
