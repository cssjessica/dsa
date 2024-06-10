class Solution:
    def longestPalindrome(self, s: str) -> int:
        # counts = defaultdict(int)
        # res = 0
        # for i in s:
        #     counts[i]+=1
        #     if counts[i] % 2 == 0:
        #         res +=2
        # for j in counts.values():
        #     if j % 2 == 1:
        #         res+=1
        #         break
        # return res

        seen = set()
        res = 0
        for i in s:
            if i in seen:
                seen.remove(i)
                res += 2
            else:
                seen.add(i)

        return res + 1 if seen else res
