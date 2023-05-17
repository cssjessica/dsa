class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(32) - O(1)
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

# or

        # res = 0
        # while n:
        #     n &= (n - 1) # n = n & (n - 1)
        #     res += 1
        # return res

