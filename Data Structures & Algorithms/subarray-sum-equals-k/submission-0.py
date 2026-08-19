class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        res = 0
        cur = 0

        for num in nums:
            cur += num
            diff = cur - k

            res += hashmap.get(diff, 0)
            hashmap[cur] = 1 + hashmap.get(cur, 0)
        
        return res