class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     k = k % len(nums)

    #     l = 0
    #     r = len(nums) - 1
    #     self.reverse(nums, l, r)
    #     print(nums)

    #     l = 0
    #     r = k - 1
    #     self.reverse(nums, l, r)

    #     l = k
    #     r = len(nums) - 1
    #     self.reverse(nums, l, r)

    # def reverse(self, arr, left, right):
    #     while left < right:
    #         arr[left], arr[right] = arr[right], arr[left]
    #         left += 1
    #         right -= 1
	
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
