class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if len(stack)>=1 and stack[-1] == "(":
                    del stack[-1]
                else:
                    return False
            elif c == "}":
                if len(stack)>=1 and stack[-1] == "{":
                    del stack[-1]
                else:
                    return False
            elif c == "]":
                if len(stack)>=1 and stack[-1] == "[":
                    del stack[-1]
                else:
                    return False
        return True if len(stack) == 0 else False
