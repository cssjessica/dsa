class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(n)

        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res
        
