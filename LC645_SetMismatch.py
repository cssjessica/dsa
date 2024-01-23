class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # # 1
        # res = [0, 0]

        # count = Counter(nums)

        # for i in range(1, len(nums) - 1):
        #     if count[i] == 0:
        #         res[1] = i
        #     if count[i] == 2:
        #         res[0] = i
        
                
        # return res

        # # 2
        # res = [0, 0]

        # for n in nums:
        #     n = abs(n)
        #     nums[n - 1] = -nums[n - 1]
        #     if nums[n - 1] > 0:
        #         res[0] = n

        # for i, n in enumerate(nums):
        #     if n > 0 and i + 1 != res[0]:
        #         res[1] = i + 1
        #         return res
                
        # 3
        N = len(nums)
        x = 0 # duplicate - missing
        y = 0 # duplicate^2 - missing^2

        for i in range(1, N + 1):
            x += nums[i - 1] - i
            y += nums[i - 1]**2 - i**2
            
        missing = (y - x**2) // (2*x)
        duplicate = missing + x
        return [duplicate, missing]
