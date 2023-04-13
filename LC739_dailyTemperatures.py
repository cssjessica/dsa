class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
			# stack monotonic decreasing order
			# time complexity: O(n)
			# memory complexity: O(n)
      stack = []
      res = [0] * len(temperatures)
      for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
          stack_t, stack_idx = stack.pop()
          res[stack_idx] = (i - stack_idx)
        stack.append([t, i])
      return res


