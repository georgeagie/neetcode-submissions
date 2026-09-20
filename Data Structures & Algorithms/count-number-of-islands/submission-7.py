class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c, grid):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] == "1" and (nr, nc) not in visited:
                    bfs(nr, nc, grid)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c, grid)
                    islands += 1
        
        return islands