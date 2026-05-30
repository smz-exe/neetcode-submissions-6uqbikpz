class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        res = []
        visited, cycle = set(), set()

        def dfs(course: int) -> bool:
            print(f"called with course: {course}")
            if course in cycle:
                return False
            
            if course in visited:
                print(f"course {course} is already visited")
                return True

            cycle.add(course)
            visited.add(course)
            print(f"course {course} added to cycle")

            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            cycle.remove(course)
            res.append(course)
            print(f"course {course} added to res")
            return True
        
        for i in range(numCourses):
            print(f"checking course {i}..")
            if not dfs(i):
                return []
            print(f"checked\n")
        
        return res
