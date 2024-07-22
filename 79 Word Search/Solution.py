# 79. Word Search
# Medium
# Topics
# Companies
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?'

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()

        def canvisit(x, y):
            return 0 <= x and x < len(board) and 0 <= y and y < len(board[0]) and (x, y) not in visited
        
        def dfs(x, y, w):
            if(len(w) == 0):
                return True

            if w[0] != board[x][y]:
                return False 
            
            if(len(w) == 1):
                return True
            
            visited.add((x, y))

            if (canvisit(x - 1, y) and dfs(x - 1, y, w[1:]) or
                canvisit(x + 1, y) and dfs(x + 1, y, w[1:]) or
                canvisit(x, y - 1) and dfs(x, y - 1, w[1:]) or
                canvisit(x, y + 1) and dfs(x, y + 1, w[1:])):
                return True
            
            visited.remove((x, y))

            return False 
        
        for x in range(len(board)):
            for y in range(len(board[0])): 
                if dfs(x, y, word): 
                    return True 
                
        return False



            
