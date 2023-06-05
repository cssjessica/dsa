class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s = ''.join(map(str, digits))
        # s = str(int(s) + 1)
        # return list(map(int, s))

        return [int(j) for j in [*str(int("".join([str(i) for i in digits])) + 1)]]
