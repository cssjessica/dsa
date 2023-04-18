class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)

        return str(list((c2-c1).keys())[0])
