# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, ptr = head, head.next
        head.next = None
        while ptr:
            next_ptr = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_ptr
        
        return prev
        
