class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # pattern: backtracking
        # data structure: 
        # main invariant
        # edge cases
        # time complexiety

        res = []
        cands = sorted(candidates)

        def dfs(start: int, cur: list[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(start, len(cands)):
                if i > start and cands[i - 1] == cands[i]:
                    continue
                
                if total + cands[i] > target:
                    break
                
                cur.append(cands[i])
                dfs(i + 1, cur, total + cands[i])
                cur.pop()

        dfs(0, [], 0)

        return res