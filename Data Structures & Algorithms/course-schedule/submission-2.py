class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq_map[crs].append(pre)
        
        visiting = set()
        def dfs(crs: int) -> bool:
            if crs in visiting:
                return False
            
            if not prereq_map[crs]:
                return True
            
            visiting.add(crs)
            for pre in prereq_map[crs]:
                if not dfs(pre):
                    visiting.remove(crs)
                    return False
            
            visiting.remove(crs)
            prereq_map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
