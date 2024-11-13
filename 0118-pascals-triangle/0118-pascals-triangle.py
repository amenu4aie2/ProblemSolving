class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x=[]
        if(numRows >=1 ):
            x.append([1])
        
        for i in range(2,numRows+1):
            x.append([1])
            y=1
            for j,k in enumerate(range(i-1,1,-1)):
                x[-1].append((x[-1][-1]*(k))//(y))
                y+=1
            x[-1].append(1)
        return x                


        