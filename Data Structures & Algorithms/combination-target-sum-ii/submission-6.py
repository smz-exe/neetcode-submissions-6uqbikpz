class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sorted_candidates = sorted(candidates)

        def dfs(start: int, cur: list[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(start, len(sorted_candidates)):
                if i > start and sorted_candidates[i - 1] == sorted_candidates[i]:
                    continue
                
                if total + sorted_candidates[i] > target:
                    break
                
                cur.append(sorted_candidates[i])
                dfs(i + 1, cur, total + sorted_candidates[i])
                cur.pop()
            
        dfs(0, [], 0)

        return res