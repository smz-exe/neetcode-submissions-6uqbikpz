class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node: int, prev: int) -> bool:
            if node in visited:
                return False
            
            visited.add(node)

            for next_node in adj[node]:
                if next_node == prev:
                    continue
                if not dfs(next_node, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n