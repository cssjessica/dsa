class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)==1:
            return mat[0][0]
        diag=0
        n=len(mat)
        for i in range(n):
                diag += mat[i][i]
                if n-i-1 != i:
                    diag += mat[i][n-i-1]
        return diag
