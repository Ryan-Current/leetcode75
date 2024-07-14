# 178 Graph Valid Tree 

# Description
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each h edge is a pair of nodes), write a function to check whether these edges make up a valid tree 

# Assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges. 

# Example 1: 
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true. 

# Example 2:
# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.

from typing import List, Dict, Set

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0: 
            return True

        graph: Dict[int, Set[int]] = {}

        for edge in edges: 
            x, y = edge[0], edge[1]

            graph.setdefault(x, set())
            graph.setdefault(y, set())

            graph[x].add(y)
            graph[y].add(x)


        visited = set()

        def dfs(node: int, previous: int): 
            if node in visited:
                return False
            
            visited.add(node)

            for next in graph[node]: 
                if next != previous and not dfs(next, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n 

n = 5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

s = Solution() 

print('Expected: true')
print(s.valid_tree(n, edges))

n = 5 
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

s = Solution() 

print('Expected: false')
print(s.valid_tree(n, edges))