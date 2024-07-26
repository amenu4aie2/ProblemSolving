import math
class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        
        return self.bs(h,p)
    def vc(self,i,p):
        hours=0
        for j in range(len(p)):
            hours+=math.ceil(p[j]/i)
        return hours
    def bs(self,h,p):
        l,r=1,max(p)
        a=0
        while l<=r:

            mid=(l+r)//2
            b=self.vc(mid,p)
            if(b<=h):
                
                a=mid
                r=mid-1
                
            elif(b>h):
                l=mid+1
            


        return a