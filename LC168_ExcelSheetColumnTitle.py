class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Time: O(log_26 (n))

        res = ""

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26
            
        return res[::-1] # reverse 