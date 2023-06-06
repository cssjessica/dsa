class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while num / 10 != 0:
            res +=num % 10
            num //= 10
            if num == 0 and res // 10 != 0:
                num = res
                res = 0

        return res
