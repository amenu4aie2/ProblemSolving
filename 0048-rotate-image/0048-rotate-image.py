class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix2=[[0]*len(matrix) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for column in range(len(matrix)):
                matrix2[row][column]=matrix[len(matrix)-1-column][row]
        matrix[:]=matrix2