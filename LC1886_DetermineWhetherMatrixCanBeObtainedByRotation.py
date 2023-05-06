class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # time complexity: O(4*n^2) = O(n^2)
        # space complexity: O(1)


        for r in range(4):
            if self.rotate_matrix(mat) == target:
                return True
        return False


    def rotate_matrix(self, matrix):

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # save the top left
                top_left = matrix[top][l + i]
                
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move top left into top right
                matrix[top + i][r] = top_left
                
            r -= 1
            l += 1

        return matrix

