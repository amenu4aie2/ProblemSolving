class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        y=sorted(nums)
        out=[]
        l,r=0,len(nums)-1
        while l<r:
            sum=y[l]+y[r]
            if(sum==target):
                out.append(nums.index(y[l]))
                out.append(len(nums)-1-(nums[::-1].index(y[r])))
                # SPACE COMPLEXITY OF ABOVE LINE IS O(N)
                # TIME COMPLEXITY OF ABOVE LINE IS O(N)(FOR INEX OPERATION) +O(N) (FOR REVERSED COPY CREATION)
                l+=1
                r-=1
                
            elif(sum<target):
                l+=1
            else:
                r-=1
        
        return out