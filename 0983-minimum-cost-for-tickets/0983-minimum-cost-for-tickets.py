class Solution:
    def mincostTickets(self, days: List[int], co: List[int]) -> int:
        arr=[0]*(days[-1])
        dp={}
        for i in days:
            arr[i-1]=1
        mincost=[float('inf')]
        def backtrack(i,c):
            # goal constraints
            
            if((i,c) in dp):
                return
            dp[(i,c)]=0
            if(i>=days[-1]):
                mincost[0]=min(mincost[0],c)

                return 
            if(c>mincost[0]):
                return
            if(any(arr[i:i+1])):

                backtrack(i+1,c+co[0])
            else:
                backtrack(i+1,c)
            if(any(arr[i:i+7])):
                backtrack(i+7,c+co[1])
            else:
                backtrack(i+7,c)
            if(any(arr[i:i+30])):
                backtrack(i+30,c+co[2])
            else:
                backtrack(i+30,c)
        backtrack(0,0)
        return mincost[0]

            