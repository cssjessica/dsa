class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        s = list(secret)
        g = list(guess)

        i, j = 0, 0
        # j is needed because it accounts for the fact that the indexes in s and g are decreasing (pop)
        while i < len(secret):
            if s[j] == g[j]:
                bull += 1
                s.pop(j)
                g.pop(j)
            else:
                j += 1
            i += 1

           
        count = Counter(s)
        for l in g:
            if l in count:
                cow += 1
                count[l] -= 1
                if count[l] == 0:
                    count.pop(l)
                
        return "{}A{}B".format(bull, cow)
