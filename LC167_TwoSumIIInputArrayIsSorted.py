class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(1)
        # similar to binary search
        # two pointers

        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            
            if total > target:
                r -= 1
            elif total < target:
                l +=1
            else:
                return [l + 1, r + 1]
