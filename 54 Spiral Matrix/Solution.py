from typing import List 

class Solution(object):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # [[1, 2, 3],
        #  [4, 5, 6],
        #  [7, 8, 9]]
        
        res = []

        current_x = 0
        current_y = 0

        min_x = 0
        min_y = 0

        max_x = len(matrix[0]) # maximum width
        max_y = len(matrix) # maximum height

        while min_x < max_x and min_y < max_y:

            # in top left
            # move all the way right 
            for i in range(min_x, max_x): 
                res.append(matrix[min_y][i])
            min_y += 1

            # in top right
            # move all the way bottom
            for i in range(min_y, max_y):
                res.append(matrix[i][max_x - 1])
            max_x -= 1

            if not (min_x < max_x and min_y < max_y):
                break

            # in bottom right
            # move all the way left
            for i in range(max_x - 1, min_x - 1, -1):
                res.append(matrix[max_y - 1][i])
            max_y -= 1

            # in bottom left
            # move all the way up
            for i in range(max_y - 1, min_y - 1, -1):
                res.append(matrix[i][min_x])
            min_x += 1

        return res

