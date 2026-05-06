class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sorted_cands = sorted(candidates)

        def dfs(idx: int, cur: list[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or idx >= len(sorted_cands):
                return
        
            cur.append(sorted_cands[idx])
            dfs(idx + 1, cur, total + sorted_cands[idx])

            cur.pop()
            while idx + 1 < len(sorted_cands) and sorted_cands[idx] == sorted_cands[idx + 1]:
                idx += 1
            dfs(idx + 1, cur, total)

        dfs(0, [], 0)
        return res