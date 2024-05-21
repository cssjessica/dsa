class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # rows, cols = len(grid), len(grid[0])

        # # flip rows
        # for r in range(rows):
        #     if grid[r][0] == 0:
        #         for c in range(cols):
        #             grid[r][c] = 0 if grid[r][c] else 1
                    
        # # flip cols
        # for c in range(cols):
        #     one_cnt = 0
        #     for r in range(rows):
        #         one_cnt += grid[r][c]
        #     if one_cnt < rows - one_cnt:
        #         for r in range(rows):
        #             grid[r][c] = 0 if grid[r][c] else 1

        # res = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         # if grid[r][c]:
        #         #     res += 2**(cols)
        #         # res += grid[r][c]
        #         res += grid[r][c] << (cols - c - 1)
        # return res


        rows, cols = len(grid), len(grid[0])
        res = rows * 2**(cols - 1)

        for c in range(1, cols):
            cnt = 0
            for r in range(rows):
                if grid[r][c] != grid[r][0]:
                    cnt += 1
            cnt = max(cnt, rows - cnt)
            res += cnt * (2**(cols - c - 1))
            
        return res
