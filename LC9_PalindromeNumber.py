class Solution:
    def isPalindrome(self, x: int) -> bool:
        # converting to string
        # c = str(x)
        # s = len(c)
        # for i in range(int(s/2)):
        #     if c[i] != c[-1-i]:
        #         return False
        # return True

        # c = str(x)
        # return c == c[::-1]

        # not converting to string

        if x < 0:
            return False
            
        div = 1
        while x >= 10 * div:
            div *= 10
            
        while x:
            right = x % 10		# get right digit
            left = x // div		# get left digit
            
            if left != right:
                return False
                
            x = x % div	# remove left digit
            x = x // 10	# remove right digit
            div = div / 100
        return True
