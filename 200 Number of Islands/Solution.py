# 200. Number of Islands
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0

        def is_unvisited(i: int, j: int) -> bool: # not out of bounds and 1
            return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0]) and grid[i][j] == '1'

        def visitNeighbors(i, j):
            grid[i][j] = "2"

            # up
            if is_unvisited(i - 1, j): 
                visitNeighbors(i - 1, j)
            
            # left 
            if is_unvisited(i, j - 1): 
                visitNeighbors(i, j - 1)

            # down
            if is_unvisited(i + 1, j): 
                visitNeighbors(i + 1, j)
            
            # right
            if is_unvisited(i, j + 1): 
                visitNeighbors(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == '1': 
                    islandCount += 1
                    visitNeighbors(i, j)

        return islandCount