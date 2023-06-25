class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

        # temp, count = 0, 0

        # for flower in flowerbed:
        #     if flower == 0:
        #         temp += 1

        #     else:
        #         if temp > 1 and temp % 2 == 1:
        #             count = temp // 2
        #             temp = 0
        #         if temp > 1 and temp % 2 == 0:
        #             count = temp // 2 - 1
        #             temp = 0
        #         temp = 0
        # return count >= n
