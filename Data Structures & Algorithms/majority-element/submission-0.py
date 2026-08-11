class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        for num, count in counter.items():
            if count > n // 2:
                return num

            