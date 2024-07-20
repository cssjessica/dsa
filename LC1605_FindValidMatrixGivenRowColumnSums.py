class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            res[r][0] = rowSum[r]
            
        for c in range(cols):
            cur_col_sum = 0
            for r in range(rows):
                cur_col_sum += res[r][c]
                
            # going the column
            r = 0
            while cur_col_sum > colSum[c]:
                diff = cur_col_sum - colSum[c]
                max_diff = min(diff, res[r][c])
                
                
                # realocate
                res[r][c] -= max_diff
                res[r][c+1] += max_diff
                cur_col_sum -= max_diff
                r+=1
                
        return res

        # res = []
        # for i in range(len(rowSum)):
        #     row = []
        #     for j in range(len(colSum)):
        #         curr = min(rowSum[i], colSum[j])
        #         rowSum[i] -= curr
        #         colSum[j] -= curr
        #         row.append(curr)
        #     res.append(row)
        # return res
