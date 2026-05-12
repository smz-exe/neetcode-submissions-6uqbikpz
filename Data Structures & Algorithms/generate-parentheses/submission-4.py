class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(n_open: int, n_close: int, cur: list[str]) -> None:
            if n_open == n_close == n:
                res.append("".join(cur))
                return
            
            if n_open < n:
                cur.append("(")
                dfs(n_open + 1, n_close, cur)
                cur.pop()
            
            if n_close < n_open:
                cur.append(")")
                dfs(n_open, n_close + 1, cur)
                cur.pop()
            
        dfs(0, 0, [])
        return res