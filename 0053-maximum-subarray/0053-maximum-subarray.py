class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=nums[0]
        cursum=0
    
        for i in nums:
            if(cursum<0):
                cursum=0
            cursum+=i
            maximum=max(maximum,cursum)
        return maximum
            