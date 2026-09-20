class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        max_area = 0

        def bfs(x, y):
            q = deque()
            count = 1
            q.append((x, y))
            grid[x][y] = 0

            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    new_r, new_c = r + dr, c + dc
                    if (new_r < 0 or new_c < 0
                        or new_r >= ROWS or new_c >= COLS
                        or grid[new_r][new_c] == 0):
                        continue
                    q.append((new_r, new_c))
                    count += 1
                    grid[new_r][new_c] = 0
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area