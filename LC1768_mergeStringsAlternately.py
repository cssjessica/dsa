class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        w1 = collections.deque(word1)
        w2 = collections.deque(word2)
        while w1 and w2:
            ans.append(w1.popleft())
            ans.append(w2.popleft())
        while w1:
            ans.append(w1.popleft())
        while w2:
            ans.append(w2.popleft())

        return "".join(ans)
