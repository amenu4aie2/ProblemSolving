class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_massive = {}

        for i, num in enumerate(nums):
            subtracter = target - num

            if subtracter in num_massive:
                return [num_massive[subtracter], i]

            num_massive[num] = i
        return []