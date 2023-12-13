class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(reversed(s.split()))

        res = collections.deque()

        i = 0
        while i < len(s):
            # skip extra white space
            if s[i] != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1
                res.appendleft(s[start: i])
                # i -= 1
            i += 1
        return " ".join(res)
