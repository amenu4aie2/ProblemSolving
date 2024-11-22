class Solution:
    def swap(self,i,j,nums):
        nums[i],nums[j]=nums[j],nums[i]
    def sortColors(self, nums: List[int]) -> None:
        low ,mid,high=0,0,len(nums)-1

        while(mid<=high):
            if(nums[mid]==0 ):
                self.swap(mid,low,nums)
                low+=1
                mid+=1
                continue
            if(nums[mid]==2):
                self.swap(mid,high,nums)
                high-=1
            
            if(nums[mid]==1):
                mid+=1
            print(nums)


        