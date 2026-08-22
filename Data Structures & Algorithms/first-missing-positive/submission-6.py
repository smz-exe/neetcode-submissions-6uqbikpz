class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1

            if 0 <= idx < n:
                nums[idx] = -abs(nums[idx]) if nums[idx] != 0 else -num
        
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1
