class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        sums = {0}

        for num in nums:
            next_sums = set(sums)

            for t in sums:
                candidate = t + num

                if candidate == target:
                    return True
                
                if candidate < target:
                    next_sums.add(candidate)
            
            sums = next_sums
        
        return False
