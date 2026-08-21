class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            hashset.add(num)
        
        for i in range(1, len(nums) + 2):
            if i not in hashset:
                return i
