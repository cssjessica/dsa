class Solution:
    def knightDialer(self, n: int) -> int:
        # time complexity: O(n)
        # space complexity: O(1)

        if n == 1:
            return 10
            
        mod = 10**9 + 7
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [1] * 10 # ways to land on i-th digit

        # state machine
        for _ in range(n - 1):
            next_dp = [0] * 10
            for n in range(10):
                for j in jumps[n]:
                    next_dp[j] = (next_dp[j] + dp[n]) % mod
            dp = next_dp
            
        res = 0
        for n in dp:
            res = (res + n) % mod
        return res
