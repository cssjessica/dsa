class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # time complexity: O(n)
        # space complexity: O(1)

        prev = bank[0].count("1")
        res = 0

        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr:
                res += (prev * curr)
                prev = curr
                
        return res
