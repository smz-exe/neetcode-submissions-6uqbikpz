class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(node: int) -> int:
            if node == parent[node]:
                return node
            
            cur = node
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            
            return cur
        
        def union(u: int, v: int) -> int:
            pu, pv = find(u), find(v)

            if pu == pv:
                return 0
            
            if rank[pu] >= rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pu]
            
            return 1
        
        res = n
        for u, v in edges:
            res -= union(u, v)
        
        return res
