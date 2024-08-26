class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n==1):
            return True
        x=3
        while (x<=n):
            if(x==n):
                return True
            x*=3
        return False
        