# 62. Unique Paths
# Medium
# Topics
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # each value represents the number of ways to get there, built 
        # bottom to top and right to left 
        # 
        # for m = 3 and n = 7 each cell represents the number of ways to arrive 
        # 
        # 28 21 15 10 6  3  1
        # 7  6  5  4  3  2  1
        # 1  1  1  1  1  1  *
        # 
        # each cell is calculated by right cell + bottom cell and the answer is in 
        # the top left cell

        # this solution only caches the previous row while building the next row 

        row = [1] * n # bottom row 

        # build rows from bottom to top, right to left
        # skipping the far right column since it will be all 1's 

        for _ in range(m - 1):
            newRow = [1] * n 
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0] 
            


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # example of the whole grid being built  
#         
#         dp = [[0 for i in range(n)] for j in range(m)]
#        
#         for i in range(n):
#             dp[0][i] = 1
#        
#         for i in range(m):
#             dp[i][0] = 1
#        
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#        
#         return dp[m-1][n-1]