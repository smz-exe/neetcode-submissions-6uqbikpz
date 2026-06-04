class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n + 1)

        def dp(i: int) -> int:
            print(f"called with {i}")
            if i == 0 or i == 1:
                print(f"base case {i}, {cost[i]}")
                return cost[i]
            
            if memo[i] != -1:
                print(f"return with {memo[i]}")
                return memo[i]
            
            if i == n:
                return min(dp(i - 1), dp(i - 2))
            
            memo[i] = min(dp(i - 2), dp(i - 1)) + cost[i]
            print(f"{i}: return with {memo[i]}")
            return memo[i]
        
        return dp(n)