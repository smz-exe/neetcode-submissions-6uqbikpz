class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = set()
        dp.add(0)

        for num in nums:
            next_dp = set()

            for t in dp:
                next_dp.add(t)

                if num + t == target:
                    return True
                
                if num + t < target:
                    next_dp.add(num + t)
            
            dp = next_dp
        
        return True if target in dp else False
