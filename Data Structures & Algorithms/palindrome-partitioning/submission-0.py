class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        pals = [[False for _ in range(n)] for _ in range(n)]
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if length == 1:
                    pals[l][r] = True
                elif length == 2:
                    if s[l] == s[r]:
                        pals[l][r] = True
                else:
                    if s[l] == s[r]:
                        pals[l][r] = pals[l + 1][r - 1]

        res = []
        part = []

        def dfs(i: int) -> None:
            if i >= n:
                res.append(part.copy())
                return
            
            for j in range(i, n):
                if pals[i][j]:
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()        

        dfs(0)
        return res