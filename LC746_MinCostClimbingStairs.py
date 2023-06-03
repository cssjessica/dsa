class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Dynamic programming
        # time complexity: O(n)
        # space complexity: O(1)
        # decision tree
        # compute backwards

        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])
