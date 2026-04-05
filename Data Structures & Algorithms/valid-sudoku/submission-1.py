class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        grids = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                n = int(board[i][j]) - 1
                mask = 1<<n
                if (rows[i] & mask
                    or cols[j] & mask
                    or grids[(i//3)*3 + j//3]&mask ):
                    return False
                rows[i] |= mask
                cols[j] |= mask
                grids[(i//3)*3+j//3] |= mask
        return True