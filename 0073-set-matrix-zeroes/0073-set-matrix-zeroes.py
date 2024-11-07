class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        column=[]
        for i in range(len(matrix)):
            if(0 in matrix[i]):
                column.extend([x for x in range(len(matrix[i])) if matrix[i][x]==0 ])
                matrix[i]=[0]*len(matrix[i])

        for i in range(len(matrix)):
            for j in column:
                matrix[i][j]=0
        