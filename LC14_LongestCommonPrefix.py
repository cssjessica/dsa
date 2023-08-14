class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # time complexity: O(nm)
        # n = min(strings)
        # m = number of strings
        # edge case: different size strings

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            
        return res
