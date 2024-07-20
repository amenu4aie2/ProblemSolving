class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[]
        for i,j in enumerate(nums):
            x.append([i,j])
        x.sort(key=lambda x:x[1])
        print(x)
        
        f,lp=0,len(nums)-1
        while f<lp:
            if(x[f][1]+x[lp][1]==target):
                return [x[f][0],x[lp][0]]
            elif(x[f][1]+x[lp][1]<target):

                f+=1
            elif(x[f][1]+x[lp][1]>target):

                lp-=1
            
        