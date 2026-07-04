class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo: dict[tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == m:
                return 1
            
            if i == n and j < m:
                return 0

            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j)
            
            return memo[(i, j)]
        
        return dfs(0, 0)
