class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = str(x)
        s = len(c)
        for i in range(int(s/2)):
            if c[i] != c[-1-i]:
                return False
        return True
#
        # c = str(x)
        # return c == c[::-1]
