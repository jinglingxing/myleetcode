class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    s[idx] = ''

        while len(stack) > 0:
            s[stack[-1]] = ''
            stack.pop()

        return ''.join(s)
