class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=nums[0]
        for i in nums[1:]:
            a=a^i
        return a