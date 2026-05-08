class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx: int, cur: list[int]) -> None:
            if idx == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[idx])
            dfs(idx + 1, cur)
            cur.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            
            dfs(idx + 1, cur)
        
        dfs(0, [])
        return res