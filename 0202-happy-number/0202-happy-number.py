class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n > 9:

            s = 0

            while n > 0:
                s += (n % 10) ** 2
                n = n // 10
            
            n = s
        
        if n == 1:
            return True
        return False