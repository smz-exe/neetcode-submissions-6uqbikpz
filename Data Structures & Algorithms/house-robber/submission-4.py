class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for n in nums:
            cur = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = cur
        
        return prev1