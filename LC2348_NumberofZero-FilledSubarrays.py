class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(1)

        i = 0
        res = 0

        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 0:
                count += 1
                i += 1
                res += count
                
            i += 1
            
        return res

        # res = 0
        # count = 0
        # for i in range(len(nums)):
        # 	if nums[i] == 0:
        # 		count += 1
        # 	else:
        # 		count = 0
        # 	res += count
        # return res
