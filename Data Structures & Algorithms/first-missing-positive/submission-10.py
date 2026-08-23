class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # negative marking
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            val = abs(num)
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -val
        
        for target in range(1, n + 1):
            if nums[target - 1] >= 0:
                return target
        
        return n + 1

