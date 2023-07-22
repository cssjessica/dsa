class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(1)

        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)
                
        return ans
