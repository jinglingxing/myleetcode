class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in dic.keys():
                stack.append(char)

            if char in dic.values():
                # When s starts with ], }, )
                if len(stack) == 0:
                    return False

                key = stack.pop()
                # When the parentheses don't match
                if dic[key] != char:
                    return False

        # stack only stores [, {, (
        return len(stack) == 0

