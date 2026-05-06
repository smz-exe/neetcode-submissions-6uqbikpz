class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(nums)

        def dfs(idx: int, cur: list[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            cur.append(candidates[idx])
            dfs(idx, cur, total + candidates[idx])
            cur.pop()
            dfs(idx + 1, cur, total)
        
        dfs(0, [], 0)
        
        return res