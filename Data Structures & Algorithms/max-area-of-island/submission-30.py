class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            cur_sum = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                cur_sum += dfs(nr, nc)
            return cur_sum
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area