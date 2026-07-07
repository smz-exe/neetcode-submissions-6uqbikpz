class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo: dict[tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if  j == m:
                return i == n
            
            first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < m and p[j + 1] == "*":
                memo[(i, j)] = (
                    dfs(i, j + 2)
                    or (first_match and dfs(i + 1, j))
                )
            else:
                memo[(i, j)] = first_match and dfs(i + 1, j + 1)

            return memo[(i, j)]

        return dfs(0, 0)
            