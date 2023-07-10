class Solution:
    def integerBreak(self, n: int) -> int:
        # time: O(n^2)
        # space: O(n)
        # dynamic programming
        # dp = {1 : 1}

        # for num in range(2, n + 1):
        #     dp[num] = 0 if num == n else num
        #     for i in range(1, num):
        #         val = dp[i] * dp[num - 1]
        #         dp[num] = max(dp[num], val)
        # return dp[n]


        # recursion
        dp = {1 : 1}

        def dfs(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]

        return dfs(n)

