# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumnode = ListNode(0)

        ptr1, ptr2, sumptr = l1, l2, sumnode
        carry = 0

        while ptr1 or ptr2 or carry:
            digit1 = ptr1.val if ptr1 else 0
            digit2 = ptr2.val if ptr2 else 0

            currSum = digit1 + digit2 + carry

            carry = currSum // 10
            newDigit = currSum % 10

            sumptr.next = ListNode(newDigit)
            
            sumptr = sumptr.next
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        
        return sumnode.next