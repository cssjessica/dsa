class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # O(nlogn + nlogk)
        res = float("inf")
        pairs = [] # (ratio, quality)
        for i in range(len(quality)):
            pairs.append((wage[i] / quality[i], quality[i]))
        pairs.sort(key=lambda p:p[0])

        max_heap = []
        total_quality = 0
        for rate, q in pairs:
            heapq.heappush(max_heap, -q)
            total_quality += q
            
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
                
            if len(max_heap) == k:
                res = min(res, total_quality * rate)
                
        return res
