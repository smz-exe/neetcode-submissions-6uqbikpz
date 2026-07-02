class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        
        memo: dict[tuple[int, int], bool] = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            if i == n and j == m:
                return True
            
            if i < n and s1[i] == s3[i + j] and dfs(i + 1, j):
                memo[(i, j)] = True
                return True
            
            if j < m and s2[j] == s3[i + j] and dfs(i, j + 1):
                memo[(i, j)] = True
                return True
            
            memo[(i, j)] = False
            return False

        return dfs(0, 0)        
