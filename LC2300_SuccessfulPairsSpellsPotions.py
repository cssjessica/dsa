class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # O(nlogm + mlogm)
        # sort potions and binary search

        potions.sort()
        res = []

        for s in spells:
            l, r = 0, len(potions) - 1
            
            while l <= r:
                m = (l+r) // 2
                if s * potions[m] >= success:
                    r = m-1
                else:
                    l = m + 1
            res.append(len(potions) - l)
        return res
