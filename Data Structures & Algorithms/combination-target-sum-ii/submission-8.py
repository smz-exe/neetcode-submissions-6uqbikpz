class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # pattern: 
        # - backtracking
        # - DFS
        # data structure: 
        # - sorted list
        # main invariant:
        # - each candidate is used at most once because recursion calles dfs(i + 1, ...)
        # - cur containes selected valuses from indices before start
        # - conbination is generated in nondecreasing order 
        # edge cases:
        # time complexity: 
        # - worst case O(n * 2^n), because each element can be chosen or skipped, and copying cur costs up to O(n)

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