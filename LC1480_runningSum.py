class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        sum_arr = []

        for n in nums:
            sum += n
            sum_arr.append(sum)

        return sum_arr
