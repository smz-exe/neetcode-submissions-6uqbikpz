class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        for i in range(len(nums)):
            res = 0 - nums[i]
            hashmap = {}
            for j in range(i+1, len(nums), 1):
                if nums[j] in hashmap:
                    triples.add(tuple(sorted([nums[i], hashmap[nums[j]], nums[j]])))
                else:
                    hashmap[res - nums[j]] = nums[j]
        return list(triples)
