class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for pr in prerequisites:
            preMap[pr[0]].append(pr[1])
        visited = set()
        def dfs(cur):
            if not preMap[cur]:
                return True
            if cur in visited:
                return False

            visited.add(cur)
            for prereq in preMap[cur]:
                if not dfs(prereq):
                    return False
            visited.remove(cur)
            preMap[cur] = []
            return True
                
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True