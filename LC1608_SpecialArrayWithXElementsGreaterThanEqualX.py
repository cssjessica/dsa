class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # nums.sort()
        # i = 0
        # prev = -1
        # total_right = len(nums)
        # while i < len(nums):
        #     if nums[i] == total_right or (prev < total_right < nums[i]):
        #         return total_right
                
        #     while i + 1 < len(nums) and nums[i] == nums[i+1]:
        #         i += 1
                
        #     prev = nums[i]
        #     i+=1
        #     total_right = len(nums) - i

        # return -1


        count = [0] * (len(nums) + 1)
        for n in nums:
            index = min(n, len(nums))
            count[index] += 1

        total_right = 0
        for i in range(len(nums), -1, -1):
            total_right += count[i]
            if i == total_right:
                return total_right
        return -1
