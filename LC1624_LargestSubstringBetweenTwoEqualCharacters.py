class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}
        res = -1

        for i, c in enumerate(s):
            if c in char_map:
                res = max(res, i - char_map[c] - 1)
            else:
                char_map[c] = i
            
        return res
