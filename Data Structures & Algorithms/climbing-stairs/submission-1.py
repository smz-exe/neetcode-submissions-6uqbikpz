class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def dp(i: int) -> int:
            if memo[i] != -1:
                return memo[i]
            
            if i == 0:
                return 1
            
            if i <= 2:
                return i
            
            memo[i] = dp(i - 1) + dp(i - 2)
            return dp(i - 1) + dp(i - 2)
        
        return dp(n)
            