from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        res = []
        def dfs(src: str) -> None:
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
            