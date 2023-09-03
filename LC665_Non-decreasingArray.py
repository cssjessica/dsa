class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # time complexity: O(n)
        # space complexity: O(1)
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
                
            # decrease left element
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            # decrease right element
            else:
                nums[i + 1] = nums[i]
            changed = True

        return True
