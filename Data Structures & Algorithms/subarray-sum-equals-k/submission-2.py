class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        cur = 0
        res = 0

        for num in nums:
            cur += num
            diff = cur - k

            if diff in hashmap:
                res += hashmap[diff]
            
            hashmap[cur] = 1 + hashmap.get(cur, 0)

        return res