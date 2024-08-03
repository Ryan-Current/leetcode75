# 21. Merge Two Sorted Lists
# Easy
# Topics
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None: 
            return list1 
    
        head = ListNode()
        current = head 
        l = list1
        r = list2

        while l is not None and r is not None: 
            if l.val < r.val: 
                current.next = l 
                l = l.next 
            else: 
                current.next = r 
                r = r.next 
            current = current.next 

        if l is None: 
            current.next = r 
        if r is None: 
            current.next = l 
        
        return head.next 

        