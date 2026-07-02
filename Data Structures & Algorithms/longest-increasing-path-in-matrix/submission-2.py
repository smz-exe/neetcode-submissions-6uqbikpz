class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        memo: dict[tuple[int, int], int] = {}

        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            
            longest = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows 
                    and 0 <= nc < cols
                    and matrix[r][c] < matrix[nr][nc] 
                ):
                    longest = max(longest, 1 + dfs(nr, nc))
            
            memo[(r, c)] = longest
            return longest

        result = 0
        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c))
        
        return result


