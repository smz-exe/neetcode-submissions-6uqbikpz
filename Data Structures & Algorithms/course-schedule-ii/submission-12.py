class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}

        for crs, req in prerequisites:
            prereq_map[crs].append(req)
        
        res = []
        visited = set()
        visiting = set()

        def dfs(i: int) -> bool:
            if i in visiting:
                return False
            
            if i in visited:
                return True
            
            visiting.add(i)

            for req in prereq_map[i]:
                if not dfs(req):
                    visiting.remove(i)
                    return False

            visiting.remove(i)
            prereq_map[i] = []
            visited.add(i)
            res.append(i)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res
        
