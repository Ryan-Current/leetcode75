# 3651 · Number of Connected Components in an Undirected Graph
# Algorithms
# Medium
# Accepted Rate
# 53%

# Description
# Solution23
# Notes
# Discuss5
# Leaderboard
# Record
# Description
# In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# You need to return the number of connected components in that graph.

# Example
# Example 1

# Input:

# 3
# [[0,1], [0,2]]
# Output:

# 1
# Example 2

# Input:

# 6
# [[0,1], [1,2], [2, 3], [4, 5]]
# Output:

# 2

# Leetcode description:
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicatesthat there is an edge between ai and bi in the graph (undirected).

# Returnthe numberof connected components in the graph


# Input: n= 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Because there are 2 separate sections of the graph
# 0 <---> 1 <---> 2
# 3 <---> 4

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i:[] for i in range(n) }

        for l, r in edges: 
            graph[l].append(r)
            graph[r].append(l)

        visited = set()

        def dfs(x: int):
            if x in visited: 
                return 
            visited.add(x)
            for n in graph[x]:
                dfs(n)
        
        count = 0

        for i in range(n):
            if i in visited:
                continue 

            count += 1
            dfs(i)

        return count


print(Solution().countComponents(5, [[0,1],[1,2],[3,4]]))