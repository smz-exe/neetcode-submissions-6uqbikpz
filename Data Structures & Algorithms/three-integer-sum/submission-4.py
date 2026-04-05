class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        n = len(nums)

        for i, a in enumerate(nums):
            target = -a
            seen = set()
            for j in range(i+1, n):
                b = nums[j]
                c = target - b
                if c in seen:
                    triples.add(tuple(sorted((a, b, c))))
                seen.add(b)
        return list(triples)
