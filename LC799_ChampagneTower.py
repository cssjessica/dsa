class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured] # flow

        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)
            # child row perspective
            for i in range(row + 1):
                left_par = prev_row[i - 1] if i > 0 else 0
                right_par = prev_row[i] if i < len(prev_row) else 0
                left_extra = max(0, left_par - 1)
                right_extra = max(0, right_par - 1)
                cur_row[i] = left_extra * 0.5 + right_extra * 0.5
                
            prev_row = cur_row
        return min(1, prev_row[query_glass])

        # for row in range(1, query_row + 1):
        #     cur_row = [0] * (row + 1)
        #     # parent row perspective
        #     for i in range(row):
        #         extra = prev_row[i] - 1
        #         if extra > 0:
        #             cur_row[i] += 0.5 * extra
        #             cur_row[i + 1] += 0.5 * extra
                
        #     prev_row = cur_row
        # return min(1, prev_row[query_glass])
