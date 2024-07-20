class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def backtrack(i,t):
            if(i>=n):
                return 1
            if((i,t) in dp):
                return dp[(i,t)]
            
            dp[(i,t)]=backtrack(i+1,t+1)+backtrack(i+2,t+2)
            return dp[(i,t)]

        return backtrack(1,0)


            
