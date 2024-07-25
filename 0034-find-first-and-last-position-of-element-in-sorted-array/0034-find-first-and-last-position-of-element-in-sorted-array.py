class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        mid=(l+r)//2
        while l<=r:
            
            if(nums[mid]==target):
                i=mid
                j=mid
                
                while((i)!=len(nums)-1 and nums[(i+1)]==target):
                    i+=1
                

                while(j!=0 and nums[j-1]==target):
                    j-=1
                    print(j)
                return [j,i]

                
            elif(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                r=mid-1
            mid=(l+r)//2
        return [-1,-1]