class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # time complexity: O(n*m)
        # # memory complexity: O(m)

        # nums1_idx = {n:i for i, n in enumerate(nums1)} # hash map O(m)
        # res = [-1] * len(nums1)

        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1_idx:
        #         continue
        #     for j in range(i + 1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = nums1_idx[nums2[i]]
        #             res[idx] = nums2[j]
        #             break
        # return res
            
        # or
        # stack monotonic
        # time complexity: O(n+m)
        # memory complexity: O(m)

        nums1_idx = {n:i for i, n in enumerate(nums1)} # hash map O(m)
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1_idx[val]
                res[idx] = cur
            if cur in nums1_idx:
                stack.append(cur)
        return res
