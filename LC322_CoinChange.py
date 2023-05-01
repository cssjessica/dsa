class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP bottom up
        # time complexity: O(a*c)
        # space complexity: O(a)


        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

        # example
        # c = [1, 3, 4, 5]
        # a = 7

