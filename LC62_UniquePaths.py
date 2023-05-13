class Solution:
		def uniquePaths(self, m: int, n: int) -> int:
            # Dynamic programming
            # compute backwards in columns for the number of rows
            # time complexity: because of the for loops O(mn) (?)
            # space complexity: #of columns O(1) constant (?)

            # row = [1] * n

            # for i in range(m - 1):
            # 	new_row = [1] * n
            # 	for j in range(n - 2, -1, -1):
            # 		new_row[j] = new_row[j + 1] + row[j]
            # 	row = new_row
            # return row[0]

            
            # updates the column as it calculates
			row = [1] * n

			for i in range(m - 1):
				for j in range(n - 2, -1, -1):
					row[j] = row[j + 1] + row[j]
			print(row)
			return row[0]
