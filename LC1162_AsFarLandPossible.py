class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    q.append([r, c])
                    
        res = -1
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            
            res = grid[r][c]
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) >= 0 and max(nr, nc) < n and grid[nr][nc] == 0):
                    q.append([nr, nc])
                    grid[nr][nc] = grid[r][c] + 1
                    
        return res - 1 if res > 1 else -1
