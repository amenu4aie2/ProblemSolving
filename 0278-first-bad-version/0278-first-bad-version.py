# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=0,n
        while(l<=r):
            mid=(l+r)//2
            if(isBadVersion(mid)==False):
                l=mid+1
            elif(isBadVersion(mid)):
                r=mid-1
            
        return l
            

