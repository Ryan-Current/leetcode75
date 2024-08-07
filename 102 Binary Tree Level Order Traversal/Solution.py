# 102. Binary Tree Level Order Traversal
# Medium
# Topics
# Companies
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res: List[List[int]] = []        

        def traverse(node: Optional[TreeNode], level: int):
            if node is None:
                return 
            
            if level > len(res) - 1: 
                res.append([])
            
            res[level].append(node.val)

            traverse(node.left, level + 1)            
            traverse(node.right, level + 1)            

        traverse(root, 0)

        return res