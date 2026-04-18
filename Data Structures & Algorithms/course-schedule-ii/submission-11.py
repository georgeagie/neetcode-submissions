class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        res = []
        visited = set()
        resolved = set()

        def dfs(curr):
            if curr in visited:
                return False
            if curr in resolved:
                return True
            
            visited.add(curr)
            for prereq in preMap[curr]:
                if not dfs(prereq):
                    return False

            res.append(curr)
            resolved.add(curr)
            visited.remove(curr)
            return True


        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
        