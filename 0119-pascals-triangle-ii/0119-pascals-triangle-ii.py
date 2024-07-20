class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate(rowIndex):
            if(rowIndex==0):
                return [[1]]
            if(rowIndex==1):
                return [[1,1]]
            
            prevrows=generate(rowIndex-1)
            prevrow=prevrows[-1]
            cur_row=[1]
            for i in range(rowIndex-1):
                cur_row.append(prevrow[i]+prevrow[i+1])
            cur_row.append(1)
            prevrows.append(cur_row)
            return prevrows
        return generate(rowIndex)[-1]