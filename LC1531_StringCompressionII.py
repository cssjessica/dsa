class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}

        def count(i, k, prev, prev_count):
            if (i, k, prev, prev_count) in cache:
                return cache[(i, k, prev, prev_count)]
            # base case
            if k < 0:
                return float("inf")
            if i == len(s):
                return 0
                
            # continue streak - do not delete mid streak
            if s[i] == prev:
                incr = 1 if prev_count in [1, 9, 99] else 0
                res = incr + count(i + 1, k, prev, prev_count + 1)
            
            # consecutive strings are different
            else:
                res = min(count(i + 1, k - 1, prev, prev_count),  # delete s[i]
                1 + count(i + 1, k, s[i], 1) # do not delete
                )
            
            cache[(i, k, prev, prev_count)] = res
            return res
            
        return count(0, k, "", 0)
