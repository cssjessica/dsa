class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer
        # memory : O(1) just pointers, not arrays
        # time: O(n)

        l, r = 0, 1 # left is buy. right is sell
        maxP = 0

        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
            r += 1
        return maxP
