class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        left, right = 0, 2**(n-1)

        for _ in range(n-1):
            mid = (left + right) // 2
            if k <= mid: # left
                right = mid
            else: # right
                left = mid + 1
                cur = 0 if cur else 1
        return cur
