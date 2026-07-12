class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        jumps = 0

        while right < len(nums) - 1:
            next_right = right
            for i in range(left, right + 1):
                next_right = max(next_right, i + nums[i])
            
            left = right + 1
            right = next_right
            jumps += 1
        
        return jumps