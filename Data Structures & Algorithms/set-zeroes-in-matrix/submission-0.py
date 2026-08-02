class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        mark = [[matrix[r][c] for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for col in range(cols):
                        mark[r][col] = 0
                    for row in range(rows):
                        mark[row][c] = 0

        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = mark[r][c]

        