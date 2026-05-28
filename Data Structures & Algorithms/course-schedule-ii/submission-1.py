class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        res = []
        visit, cycle = set(), set()

        def dfs(course: int) -> bool:
            if course in cycle:
                return False
            
            if course in visit:
                return True
            
            cycle.add(course)

            for prereq in prereq_map[course]:
                if dfs(prereq) == False:
                    return False
            
            cycle.remove(course)
            visit.add(course)
            res.append(course)
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return res
            