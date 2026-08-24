from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

            if len(counter) <= 2:
                continue
            
            new_counter = defaultdict(int)
            for cand, c in counter.items():
                if c > 1:
                    new_counter[cand] = c - 1
            
            counter = new_counter
        
        res = []
        for num in counter:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res