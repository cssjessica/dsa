class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n >>= 1 == n/=2
        # (n & 1) == n % 2
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
