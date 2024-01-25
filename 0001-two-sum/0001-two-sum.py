class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {i:j for j,i in enumerate(nums)}
        for k,i in enumerate(nums):
            if target-i in n:
                if k==n[target-i]:continue
                return [k,n[target-i]]
        return [0]