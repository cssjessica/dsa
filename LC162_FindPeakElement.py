class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # time complexity: O(log n)

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            
            # left neighbor greater
            if m > 0 and nums[m - 1] > nums[m]:
                r = m - 1
            
            # right neighbor greater
            elif m < len(nums) - 1 and nums[m + 1] > nums[m]:
                l = m + 1
            
            else:
                return m
