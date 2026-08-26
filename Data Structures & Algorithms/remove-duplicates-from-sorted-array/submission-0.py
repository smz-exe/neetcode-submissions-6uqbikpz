class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        
        for num in nums:
            if num in seen:
                continue
            
            seen.add(num)
            nums[i] = num
            i += 1
        
        return i
