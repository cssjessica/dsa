class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recursive
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        dp = {(m-1, n-1): 1}

        def dfs(r, c):
            if r == m or c == n or grid[r][c]:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return dp[(r,c)]
        return dfs(0,0)

        # # dynammic programming
        # grid = obstacleGrid
        # m, n = len(grid), len(grid[0])
        # dp = [0] * n
        # dp[n-1] = 1

        # for r in reversed(range(m)):
        #     for c in reversed(range(n)):
        #         if grid[r][c]:
        #             dp[c] = 0
        #         elif c+1 < n:
        #             dp[c] = dp[c] + dp[c+1]
                    
        # return dp[0]
