class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            print(i)
            last = min(nums[i] + i, n - 1)
            print(last)
            print(dp[last])

            count = float("inf")
            for j in range(last, i, -1):
                print(f"j: {j}")
                count = min(count, dp[j])
            
            dp[i] = count + 1
            print(dp[i])
        
        return dp[0]