class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # unique = []
        # for i, num in enumerate(nums[:-1]):
        #     if num != nums[i+1]:
        #         unique.append(num)
        #         if nums[i+1] == nums[-1]:
        #             unique.append(nums[i+1])
            
        # return len(unique)
        
        # Two pointers
        # Time complexity: O(n)

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l



