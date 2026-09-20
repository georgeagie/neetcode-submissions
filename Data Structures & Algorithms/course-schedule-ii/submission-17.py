class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()
        added = set()
        ordering = []
        def dfs(crs):
            if crs in added:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            ordering.append(crs)
            added.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return ordering