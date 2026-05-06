class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(nums)

        def dfs(start: int, cur: list[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    return
                
                cur.append(candidates[i])
                dfs(i, cur, total + candidates[i])
                cur.pop()
        
        dfs(0, [], 0)

        return res