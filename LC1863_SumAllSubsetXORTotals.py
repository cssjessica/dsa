class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # def dfs(i, total):
        #     if i == len(nums):
        #         return total
                
        #     return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
            
        # return dfs(0, 0)

        res = 0
        for n in nums:
            res = res | n
        return res * 2**(len(nums) - 1)
