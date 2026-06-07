class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def helper(arr: list[int]) -> int:
            prev2, prev1 = 0, 0

            for num in arr:
                cur = max(prev2 + num, prev1)
                prev2 = prev1
                prev1 = cur
            return prev1
        
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[1:]), helper(nums[:-1]))