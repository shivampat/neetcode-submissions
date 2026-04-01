# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        ptr = head

        while ptr:
            count += 1
            ptr = ptr.next
        
        dummy = ListNode(0, head)
        to_remove, prev = dummy, None

        for i in range(count + 1 - n):
            prev = to_remove
            to_remove = to_remove.next
        
        prev.next = to_remove.next

        return dummy.next

        
