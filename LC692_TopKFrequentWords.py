class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = [(-count, word) for word, count in counts.items()] # O(n)
        heapq.heapify(heap) # O(n)
        return [heapq.heappop(heap)[1] for _ in range(k)] # O(logn)

