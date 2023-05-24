class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        strn = str(n)
        for i in strn:
            prod *= int(i)
            summ += int(i)
        return prod - summ
