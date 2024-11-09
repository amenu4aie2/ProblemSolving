class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        y=[[1],[1,1]]
        if(numRows==1):
            return [[1]]
            
        elif(numRows==2):
            return y
        else:
            for i in range(2,numRows):
                y.append([1])
                for i in range(len(y[-2])-1):
                    y[-1].append(y[-2][i]+y[-2][i+1])
                y[-1].append(1)

        return y