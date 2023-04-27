class Solution:
    def decodeString(self, s: str) -> str:
        # stack or recursive approaches
        # stack
        # time complexity: O(n)

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr # join by the left
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # join by the left
                stack.append(int(k) * substr)
        print(stack)
        return "".join(stack)

