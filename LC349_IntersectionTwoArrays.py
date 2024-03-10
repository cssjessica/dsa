class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        res = []

        for n1 in nums1:
            seen.add(n1)
            
        for n2 in nums2:
            if n2 in seen:
                res.append(n2)
                seen.remove(n2)
        return res
