# 230. Kth Smallest Element in a BST
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # maybe run a preorder traversal until you find the kth smallest int?
        # it's a bst which means if there is no left, then it is smallest, so maybe pop it or something

        k -= 1
        res = None
        def preorder(node):
            nonlocal k
            nonlocal res
            if node is None: 
                return 
            
            preorder(node.left)
            
            if res is not None:
                return 

            if k > 0:
                k -= 1
            else:
                res = node.val
                return 
            
            preorder(node.right)

        preorder(root)

        return res
            