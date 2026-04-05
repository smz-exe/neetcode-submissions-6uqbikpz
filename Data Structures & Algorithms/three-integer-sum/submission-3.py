class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        for i, a in enumerate(nums):
            hashmap = {}
            target = 0 - a
            for j in range(i+1, len(nums), 1):
                if nums[j] in hashmap:
                    triples.add(tuple(sorted([a, hashmap[nums[j]], nums[j]])))
                else:
                    hashmap[target - nums[j]] = nums[j]
        print(triples)
        return list(triples)
