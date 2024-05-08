class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # finding the decreasing subsequence
        ds=0
        for i in range(len(nums)-1):
            if(nums[i+1]>nums[i]):
                ds=i+1
            else:
                pass
        # swapping two elements and then sorting from that value to the end
        ds=ds-1
        
        nums[ds+1:]=sorted(nums[ds+1:])
        for i in range(len(nums[ds+1:])):
            if(nums[ds]<nums[i+ds+1]):
                nums[ds],nums[i+1+ds]=nums[i+1+ds],nums[ds]
                break
        # nums[ds],nums[x]=nums[x],nums[ds]
        # print(x)
        
        print(nums)
        return nums