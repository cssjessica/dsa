class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # # time complexity: O(nm)
        # # space complexity: O(nm)

        # rows, cols = len(img), len(img[0])

        # res = [[0] * cols for _ in range(rows)]

        # for r in range(rows):
        #     for c in range(cols):
        #         total, count = 0, 0
        #         for i in range(r - 1, r + 1 + 1):
        #             for j in range(c - 1, c + 1 + 1):
        #                 if i < 0 or i == rows or j < 0 or j == cols:
        #                     continue
        #                 total += img[i][j]
        #                 count += 1
        #         res[r][c] = total // count
                
        # return res

        # time complexity: O(nm)
        # space complexity: O(1)

        rows, cols = len(img), len(img[0])

        for r in range(rows):
            for c in range(cols):
                total, count = 0, 0
                for i in range(r - 1, r + 1 + 1):
                    for j in range(c - 1, c + 1 + 1):
                        if i < 0 or i == rows or j < 0 or j == cols:
                            continue
                        total += img[i][j] % 256
                        count += 1
                # shift the result 8 bits to the left
                img[r][c] = img[r][c] ^ (total // count) << 8
                
        # shifts the result 8 bits to the right
        for r in range(rows):
            for c in range(cols):
                img[r][c] = img[r][c] >> 8
                
        return img
