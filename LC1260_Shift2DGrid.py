class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # time complexity: O(mn)
        # space complexity: O(mn)

        M, N = len(grid), len(grid[0])

        # map 2d to 1d
        def posToVal(r, c):
            return r * N + c

        # map 1d to 2d
        def valToPos(v):
            return  [v // N, v % N] # r, c
            
        res = [[0] * N for i in range(M)]
        # shift by k
        for r in range(M):
            for c in range(N):
                newInd = (posToVal(r, c) + k) % (M * N)
                newR, newC = valToPos(newInd)
                res[newR][newC] = grid[r][c]
        return res
