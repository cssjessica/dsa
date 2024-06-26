class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # zero - one knapsack - DP

        dp = {}

        for i in range(len(questions) - 1, -1, -1):
            dp[i] = max(questions[i][0] + dp.get(i + 1 + questions[i][1], 0), dp.get(i+1, 0))
        return dp[0]


        # ds = {}
        # def dfs(i):
        #     if i >= len(questions):
        #         return 0
        #     if i in ds:
        #         return ds[i]
                
        #     ds[i] = max(dfs(i+1), questions[i][0] + dfs(i + 1 + questions[i][1]))
            
        #     return ds[i]
        # return dfs(0)
