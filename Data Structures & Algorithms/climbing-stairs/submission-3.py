class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def dfs(i: int):
            if i <= 2:
                memo[i] = i
                return memo[i]
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]
        
        return dfs(n)
            

            