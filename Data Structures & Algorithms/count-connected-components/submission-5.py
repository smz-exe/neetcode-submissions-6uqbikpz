class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(node: int) -> int:
            cur = node

            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            
            return cur
        
        def union(u: int, v: int) -> int:
            pu, pv = find(u), find(v)

            if pu == pv:
                return 0
            
            if size[pu] >= size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
            
            return 1
        
        components = n
        for u, v in edges:
            components -= union(u, v)
        
        return components