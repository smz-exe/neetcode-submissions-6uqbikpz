class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        dp = {0}

        for num in nums:
            next_dp = set(dp)

            for t in dp:
                new_sum = num + t

                if new_sum == target:
                    return True
                
                if new_sum < target:
                    next_dp.add(new_sum)
            
            dp = next_dp
        
        return False