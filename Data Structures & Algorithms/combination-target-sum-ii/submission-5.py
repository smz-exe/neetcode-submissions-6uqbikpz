class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sorted_cands = sorted(candidates)

        def dfs(start: int, cur: list[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(start, len(sorted_cands)):
                if i > start and sorted_cands[i - 1] == sorted_cands[i]:
                    continue
                
                if total + sorted_cands[i] > target:
                    return
                
                cur.append(sorted_cands[i])
                dfs(i + 1, cur, total + sorted_cands[i])
                cur.pop()
            
        dfs(0, [], 0)
            
        return res
                
