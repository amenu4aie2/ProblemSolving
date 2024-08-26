class Solution:
    def addDigits(self, num: int) -> int:
        nums=str(num)
        while (len(nums)>1):
            x=0
            for i in nums:
                x+=int(i)
            nums=str(x)
        return int(nums)