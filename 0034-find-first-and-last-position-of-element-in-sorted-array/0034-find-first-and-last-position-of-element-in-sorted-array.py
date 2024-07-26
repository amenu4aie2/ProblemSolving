class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarSearch(nums,0,target),self.binarSearch(nums,1,target)]

    def binarSearch(self,n,b,t):
        l,r=0,len(n)-1
        i=-1
        while(l<=r):
            mid=(l+r)//2
            if(n[mid]<t):
                l=mid+1



            elif(n[mid]>t):
                r=mid-1
            else:
                i=mid
                if b:
                    l=mid+1
                else:
                    r=mid-1
        
        return i