class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        cur = 0
        res = 0

        for num in nums:
            cur += num
            # sum(nums[i: j] = prefix[j] - prefix[i]
            prefix = cur - k
            if prefix in hashmap:
                res += hashmap[prefix]
            hashmap[cur] = 1 + hashmap.get(cur, 0)
        
        return res