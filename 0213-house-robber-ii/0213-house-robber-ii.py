from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtracking(i, memo,nums):
            print(nums)
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            rob_current = nums[i] + backtracking(i + 2, memo,nums)
            skip_current = backtracking(i + 1, memo,nums)
            memo[i] = max(rob_current, skip_current)

            return memo[i]
        
        def hair(nums):
            if len(nums) > 2:
                a = nums[-1]
                nums = nums[:-1].copy()
                one = backtracking(0, {},nums)
                nums.append(a)
                nums = nums[1:]
                two = backtracking(0, {},nums)
                return max(one, two)
            else:
                return max(nums)
        
        return hair(nums)


