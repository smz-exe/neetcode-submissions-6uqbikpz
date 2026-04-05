class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == ".":
                    continue
                if ( n in rows[i]
                    or n in cols[j]
                    or n in grids[(i//3, j//3)] ):
                    return False
                
                rows[i].add(n)
                cols[j].add(n)
                grids[(i//3, j//3)].add(n)

        return True

