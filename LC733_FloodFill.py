class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]    		        # gets color for the source pixel
        self.dfs(image, sr, sc, color, starting_pixel)	# run dfs for the source pixel

        return image

    def dfs(self, image, sr, sc, new_color, starting_pixel):
        # Check: 1. higher than boundary bottom, 2. lower than boundary top, 3. higher than boundary left, 4. lower than boundary right, 5. color of the current point is equal to the new color (act as a boundary to not go run the code further in that point (?)), 6. color of the current point is different from the original color (act as a boundary).
        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == new_color or image[sr][sc] != starting_pixel:
            return
            
        image[sr][sc] = new_color
        self.dfs(image, sr + 1, sc, new_color, starting_pixel) # bottom
        self.dfs(image, sr - 1, sc, new_color, starting_pixel) # top
        self.dfs(image, sr, sc + 1, new_color, starting_pixel) # right
        self.dfs(image, sr, sc - 1, new_color, starting_pixel) # left
