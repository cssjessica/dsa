class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # base case: nrows = 1
        if numRows == 1:
            return s
            
        res = ""

        for r in range(numRows):
            add = 2 * (numRows - 1)
            for i in range(r, len(s), add):
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + add - 2 * r < len(s)):
                    res += s[i + add - 2 * r]
                    
        return res
