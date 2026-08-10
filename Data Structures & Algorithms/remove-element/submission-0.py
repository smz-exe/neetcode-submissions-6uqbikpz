class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = len(nums)

        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                count -= 1
            else:
                i += 1
            
        return count