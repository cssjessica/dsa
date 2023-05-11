class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum(range(len(n+1))) - sum(nums) = n not in nums
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
