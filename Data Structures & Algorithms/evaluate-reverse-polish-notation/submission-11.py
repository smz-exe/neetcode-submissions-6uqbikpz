class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack[-1] if stack else "empty")
            if t == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif t == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif t == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif t == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(t))

        
        return stack[-1]