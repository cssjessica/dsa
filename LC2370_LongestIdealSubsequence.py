class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        res = 0

        for c in s:
            curr = ord(c) - ord('a') # 0 - 25
            longest = 1
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = max(dp[curr], longest)
            
        return max(dp)

        # cache = {}

        # def helper(i, prev):
        #     if i == len(s):
        #         return 0
        #     if (i, prev) in cache:
        #         return cache[(i, prev)]
                
        #     res = helper(i + 1, prev) # skip s[i]
            
        #     if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
        #         res = max(res, 1 + helper(i + 1, s[i]))
        #     cache[(i, prev)] = res
        #     return res
        # return helper(0, "")
	
