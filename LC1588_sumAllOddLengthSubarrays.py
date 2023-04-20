class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for k in range(1, n+1, 2):
            for t in range(n-k+1):
                total += sum(arr[t:t+k])
        return total
