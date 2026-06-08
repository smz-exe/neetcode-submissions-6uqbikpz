class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}

        for crs, req in prerequisites:
            prereq_map[crs].append(req)
        
        visiting = set()
        visited = set()
        order = []

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
            
            prereq_map[crs] = []
            visiting.remove(crs)
            order.append(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order
            
        

