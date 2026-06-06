class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:]
        dp.append(0)
        n = len(dp)

        for i in range(n - 3, -1, -1):
            dp[i] = dp[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])
