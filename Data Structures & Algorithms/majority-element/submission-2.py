class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
            
            if res == num:
                count += 1
            else:
                count -= 1
        
        return res

