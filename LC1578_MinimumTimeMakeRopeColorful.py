class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # if two adjacent baloons same color, pop the one with less needed time
        l = res = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
        return res
