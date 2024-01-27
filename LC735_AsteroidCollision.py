class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(n)
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0 # break out of the loop
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
                
        return stack
