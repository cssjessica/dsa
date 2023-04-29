class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        # time complexity: O(log n)
        # space complexity: O(1)
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
