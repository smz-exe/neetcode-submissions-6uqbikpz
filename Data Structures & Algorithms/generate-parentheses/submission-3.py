class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(n_open: int, n_close: int, cur: list[str]) -> None:
            if n_open == n_close == n:
                res.append("".join(stack))
                return
            
            if n_open < n:
                stack.append("(")
                backtrack(n_open + 1, n_close, stack)
                stack.pop()
            
            if n_close < n_open:
                stack.append(")")
                backtrack(n_open, n_close + 1, stack)
                stack.pop()
        
        backtrack(0, 0, [])
        return res