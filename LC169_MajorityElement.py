class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time O(n) 
        # space O(1)
        # Boyer Moore Algorithm
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res


        # time O(n) 
        # space O(n)
        # count = {}
        # res, maxCount = 0, 0

        # for n in nums:
        # 	count[n] = 1 + count.get(n, 0)
        # 	if count[n] > maxCount:
        # 		res = n
        # 	maxCount = max(count[n], maxCount)
        # return res
