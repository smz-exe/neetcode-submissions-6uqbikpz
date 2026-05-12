class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        is_pal = [[False for _ in range(n)] for _ in range(n)]

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length <= 2 or is_pal[l + 1][r - 1]):
                    is_pal[l][r] = True
        
        res = []
        part = []

        def dfs(i: int) -> None:
            if i == n:
                res.append(part.copy())
                return
            
            for j in range(i, n):
                if is_pal[i][j]:
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
            
        