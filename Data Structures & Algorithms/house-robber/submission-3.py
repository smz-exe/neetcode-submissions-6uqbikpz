class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo = [-1] * n
        def dp(i: int) -> int:
            if i == n - 1 or i == n - 2:
                return nums[i]
            
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return memo[i]
        
        return max(dp(0), dp(1))
