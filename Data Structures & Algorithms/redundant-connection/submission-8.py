class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node: int) -> int:
            cur = node

            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            
            return cur
        
        def union(u: int, v: int) -> bool:
            pu, pv = find(u), find(v)

            if pu == pv:
                return False
            
            if size[pu] >= size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]

            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []
