class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # could use heap O(klog n)
        # use bucket sort O(n)

        count = {}
        freq = [[] for i in range(len(nums) + 1)] # O(n)

        for n in nums: # O(n)
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): # <O(n)
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1): # O(n)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

