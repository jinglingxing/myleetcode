class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_, close = 0, 0
        stack = []
        temp = ""
        for char in s:
            if char == '(':
                open_ += 1
            else:
                close += 1

            temp += char
            # put the primitive valid parentheses strings in a stack
            if open_ == close:
                stack.append(temp)
                temp = ""

        # remove the Outermost Parentheses for each string in the stack
        res = ""
        for str_ in stack:
            print(str_)
            res += str_[1: len(str_) - 1]

        return res

