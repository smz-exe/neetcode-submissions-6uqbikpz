class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))
        size = [1] * n

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
                return False
        return True