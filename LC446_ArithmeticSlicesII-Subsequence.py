class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # time complexity: O(n^2)
        # space complexity: O(n^2)
        
        res, n = 0, len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        # dp[i][diff] # of subseq ending at i with diff

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff]
                
        return res
