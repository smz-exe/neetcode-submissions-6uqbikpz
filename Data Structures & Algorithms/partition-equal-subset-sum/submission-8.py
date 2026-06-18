class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        dp = {0}

        for num in nums:
            new_sum = set(dp)

            for t in dp:
                candidate = t + num

                if candidate == target:
                    return True
                
                if candidate < target:
                    new_sum.add(candidate)
            
            dp = new_sum
        
        return False
