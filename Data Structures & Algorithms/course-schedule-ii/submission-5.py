class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        res = []
        visiting = set()
        visited = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)

            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                visiting = set()
                return []
        
        return res
