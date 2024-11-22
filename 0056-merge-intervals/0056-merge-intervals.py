class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        x=[]
        for i in range(len(intervals)):

            if(x and x[-1][1]>=intervals[i][0]):
                x[-1][1]=max(x[-1][1],intervals[i][1])
                continue
            x.append(intervals[i]) 
        return x 