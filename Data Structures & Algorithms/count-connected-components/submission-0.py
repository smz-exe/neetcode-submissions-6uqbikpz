class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = 0
        visited = set()

        def dfs(i: int) -> None:
            if i in visited:
                return
            
            visited.add(i)
            for j in adj[i]:
                dfs(j)


        for i in range(n):
            if i in visited:
                continue
            
            dfs(i)
            res += 1

        return res