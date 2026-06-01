class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}

        for crs, req in prerequisites:
            prereq_map[crs].append(req)
        
        visiting = set()
        visited = set()
        res = []

        def dfs(crs: int) -> bool:
            print(f"called with {crs}")
            if crs in visiting:
                return False
            
            if crs in visited:
                return True

            visiting.add(crs)

            for req in prereq_map[crs]:
                if not dfs(req):
                    return False
            
            prereq_map[crs] = []
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res

