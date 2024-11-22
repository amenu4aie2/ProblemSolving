import numpy as np
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix in-place using numpy.
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Convert matrix to a numpy array
        matrix_np = np.array(matrix)
        
        # Step 2: Reverse rows and transpose
        matrix_np = np.transpose(matrix_np[::-1])
        
        # Step 3: Copy values back to the original matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix_np[i][j])
