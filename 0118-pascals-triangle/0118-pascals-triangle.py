class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t=[[1],[1,1],[1,2,1]]
        if(numRows==1 or numRows==2 or numRows==2):
            return t[:numRows]

        for i in range(2,numRows-1):
            x=len(t[-1])
            t.append([1])
            for j in range(x-1):
                t[-1].append(t[-2][j]+t[-2][j+1])
            t[-1].append(1)
        print(t)
        return t