class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtracking(i,memo):
            
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            rob_curent=nums[i]+backtracking(i+2,memo)

            skip_cure= backtracking(i+1,memo)


            memo[i]=max(rob_curent,skip_cure)

            return memo[i]
        return backtracking(0,{})