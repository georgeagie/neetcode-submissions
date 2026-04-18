class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}

        for i in range(numCourses):
            preMap[i] = []

        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)
        
        print(preMap)
        
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            if preMap[curr] == []:
                return True

            visited.add(curr)
            for prereq in preMap[curr]:
                if not dfs(prereq):
                    return False
            
            visited.remove(curr)
            preMap[curr] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
