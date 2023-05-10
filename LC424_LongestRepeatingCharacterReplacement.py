class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # time complexity: O(26s) - O(s)
        # space complexity: O(1)(?)

        # 1

        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # this max checks every value in the dict
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res

# 2
        # count = {}
        # res = 0

        # l = 0
        # maxf = 0
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxf = max(maxf, count[s[r]])
        #     # this updates/calculates maxf only when needed
            
        #     while (r - l + 1) - maxf > k:
        #         count[s[l]] -= 1
        #         l += 1
                
        #     res = max(res, r - l + 1)

        # return res
