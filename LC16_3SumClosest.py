class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums[1] + nums[-1]
        nums.sort()

        for i in range(len(nums)- 2):
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > target:
                    r -= 1
                else:
                    l += 1
                if abs(threeSum - target) < abs(res - target):
                    res = threeSum

        return res
