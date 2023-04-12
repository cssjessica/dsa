class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n != r*c:
            return mat
        else:
            new_mat=[]
            new_row=[]
            for i in range(m):
                for j in range(n):
                    new_row.append(mat[i][j])
                    if len(new_row)==c:
                        new_mat.append(new_row)
                        new_row=[]
                
            return new_mat
        
