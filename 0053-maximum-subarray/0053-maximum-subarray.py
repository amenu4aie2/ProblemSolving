class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=float('-inf')
        currentmax=float('-inf')
        sum=float('-inf')
        for i in nums:
            if(i>i+sum):
                sum=i
                
            else:
                sum+=i
            s=max(sum,s)

        return s