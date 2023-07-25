class Solution:
    def removeStars(self, s: str) -> str:
        # Time complexity: O(len(s))
        # Space complexity: O(len(s))
        stack = []

        for c in s:
            if c == "*":
                stack and stack.pop()
            
            else:
                stack.append(c)

        return "".join(stack)
