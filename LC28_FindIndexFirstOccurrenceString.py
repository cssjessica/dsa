class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # time complexity: O(n * m)
        # space complexity: O(1)

        if needle == " ":
            return 0
            
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
