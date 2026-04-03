# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, None)

        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        ptr, prev = slow.next, None
        slow.next = None

        while ptr:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        
        ptrL, ptrR = head, prev
        ptr = dummy.next

        while ptrL and ptrR:
            tmpL, tmpR = ptrL.next, ptrR.next

            ptrL.next = ptrR
            ptrR.next = tmpL

            ptrL = tmpL
            ptrR = tmpR
            