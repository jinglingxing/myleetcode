class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_ = 0

        for char in s:
            if char == '(':
                stack.append('(')
                max_ = max(len(stack), max_)
            elif char == ')':
                stack.pop()

        return max_