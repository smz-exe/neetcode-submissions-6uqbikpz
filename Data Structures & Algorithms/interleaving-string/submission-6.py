class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if n + m != len(s3):
            return False

        dp: dict[tuple[int, int], bool] = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == n and j == m:
                return True
            
            if i < n and s1[i] == s3[i + j] and dfs(i + 1, j):
                dp[(i, j)] = True
                return True
            
            if j < m and s2[j] == s3[i + j] and dfs(i, j + 1):
                dp[(i, j)] = True
                return True
            
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)