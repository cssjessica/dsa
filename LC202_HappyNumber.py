class Solution:
    def isHappy(self, n: int) -> bool:
        # still have to try solving it with linked list cycle
        # hash set
        visit = set() # memory O(n)

        while n not in visit:
            visit.add(n)
            n = self.sum_squares(n)
            
            if n == 1:
                return True
                
        return False
	
    def sum_squares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
        
	
