from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

            if len(counter) <= 2:
                continue
            
            new_counter = defaultdict(int)
            for cand, count in counter.items():
                if count > 1:
                    new_counter[cand] = count - 1
            
            counter = new_counter
        
        res = []
        for cand in counter:
            if nums.count(cand) > len(nums) // 3:
                res.append(cand)

        return res