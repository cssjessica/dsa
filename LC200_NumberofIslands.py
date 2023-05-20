class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
# water is 0
# land is 1
# flood fill land with 2
# time complexity: O(mn) + O(N), N = number of cells in flood fill = O(mn) + O(mn) = O(mn)
# Space complexity: O(mn)

        n = len(grid)	    # n rows
        m = len(grid[0])	# n columns
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    self.flood_fill(grid, i, j, "2")
        return count
        
    def flood_fill(self, grid, i, j, value):
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] != "1":
            return
            
        grid[i][j] = value
        self.flood_fill(grid, i + 1, j, value)
        self.flood_fill(grid, i - 1, j, value)
        self.flood_fill(grid, i, j + 1, value)
        self.flood_fill(grid, i, j - 1, value)
