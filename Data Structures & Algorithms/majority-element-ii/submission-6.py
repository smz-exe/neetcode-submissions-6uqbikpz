from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            count = new_count
        
        res = []
        for cand in count:
            if nums.count(cand) > len(nums) // 3:
                res.append(cand)
        
        return res
            