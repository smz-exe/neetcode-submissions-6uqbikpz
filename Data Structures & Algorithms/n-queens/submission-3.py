class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()

        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(r: int) -> None:
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if (
                    c not in cols
                    and (r + c) not in pos_diag
                    and (r - c) not in neg_diag
                ):
                    cols.add(c)
                    pos_diag.add(r + c)
                    neg_diag.add(r - c)
                    board[r][c] = "Q"

                    dfs(r + 1)

                    cols.remove(c)
                    pos_diag.remove(r + c)
                    neg_diag.remove(r - c)        
                    board[r][c] = "."
        
        dfs(0)
        return res