class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}

        for crs, req in prerequisites:
            prereq_map[crs].append(req)
        
        res = []
        visiting = set()
        visited = set()

        def dfs(crs: int) -> bool:
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visiting.add(crs)

            for req in prereq_map[crs]:
                if not dfs(req):
                    visiting.remove(crs)
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res