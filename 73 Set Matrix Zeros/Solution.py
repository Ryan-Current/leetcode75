from typing import List

class Solution(object):
    def setZeroes(self, matrix: List[List[int]]):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # mark all rows and columns that should be zero'd 

        top_left = matrix[0][0]

        for x in range(0, len(matrix)): 
            for y in range(0, len(matrix[x])):
                if matrix[x][y] == 0:
                    if x == 0: 
                        top_left = 0
                    else: 
                        matrix[x][0] = 0 # set the leftmost column to be 0'd, unless it is in the top row 
                    matrix[0][y] = 0 # set the topmost column to be 0'd 

        # take care of rows 1 and on
        for x in range(1, len(matrix)):
            if matrix[x][0] == 0: 
                for y in range(0, len(matrix[x])):
                    matrix[x][y] = 0
        
        # take care of columns 0 and on
        for y in range(0, len(matrix[0])):
            if matrix[0][y] == 0: 
                for x in range(0, len(matrix)):
                    matrix[x][y] = 0

        # take care of first row 
        if top_left == 0: 
            for y in range(0, len(matrix[0])):
                matrix[0][y] = 0
            
    

            

        

