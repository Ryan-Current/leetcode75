# 19. Remove Nth Node From End of List
# Medium
# Topics
# Companies
# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_back = None 
        current = head

        while current is not None:
            current = current.next

            if n == 0: 
                if n_back is None:
                    n_back = head 
                else: 
                    n_back = n_back.next
            else: 
                n -= 1
                
            if(current is None):
                if n_back is None: 
                    head = head.next
                else: 
                    n_back.next = n_back.next.next 
                return head 
