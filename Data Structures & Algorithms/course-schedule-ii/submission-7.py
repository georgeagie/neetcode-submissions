class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        print(preMap)
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
                print(curr)
                if not dfs(prereq):
                    return False

            res.append(curr)
            resolved.add(curr)
            visited.remove(curr)
            print(res)
            return True


        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
        