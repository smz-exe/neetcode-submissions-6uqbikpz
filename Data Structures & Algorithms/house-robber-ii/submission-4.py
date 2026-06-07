class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(l: int, r: int) -> int:
            prev2, prev1 = 0, 0

            for i in range(l, r + 1):
                cur = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = cur

            return prev1
        
        if len(nums) == 1:
            return nums[0]
        
        return max(
            helper(0, len(nums) - 2),
            helper(1, len(nums) - 1)
        )