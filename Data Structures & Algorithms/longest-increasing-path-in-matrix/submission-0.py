class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        memo: dict[tuple[int, int], int] = {}

        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            
            path = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < n 
                    and 0 <= nc < m
                    and matrix[r][c] < matrix[nr][nc] 
                ):
                    path = max(path, 1 + dfs(nr, nc))
            
            memo[(r, c)] = path
            return memo[(r, c)]

        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, dfs(r, c))
        
        return res


