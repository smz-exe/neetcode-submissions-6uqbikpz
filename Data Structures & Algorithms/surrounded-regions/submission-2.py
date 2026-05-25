from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def capture(r, c):
            out_of_bounds = r < 0 or c < 0 or r >= rows or c >= cols
            if (
                out_of_bounds
                or board[r][c] != "O"
            ):
                return
            
            board[r][c] = "T"
            for dr, dc in directions:
                capture(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if (
                    board[r][c] == "O"
                    and (r in (0, rows - 1) or c in (0, cols - 1))
                ):
                    capture(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        