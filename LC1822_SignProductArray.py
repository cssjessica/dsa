class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # product = 1
        # for i in range(len(nums)):
        #     product *= nums[i]

        # if product > 0:
        #     return 1
        # elif product == 0:
        #     return 0
        # else:
        #     return -1

        count = 0
        for num in nums:
            if num == 0: return 0
            if num < 0:
                count += 1
        if count % 2 == 0:
            return 1
        else:
            return -1
