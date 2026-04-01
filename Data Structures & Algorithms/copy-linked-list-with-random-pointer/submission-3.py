"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNewMap = {None: None}

        ptr, prev = head, None
        while ptr:
            new = Node(ptr.val)

            if prev:
                prev.next = new

            oldNewMap[ptr] = new

            prev = new 
            ptr = ptr.next
        
        ptr = head
        while ptr:
            oldRandom = ptr.random
            if oldRandom:
                oldNewMap[ptr].random = oldNewMap[oldRandom]
            ptr = ptr.next
        
        return oldNewMap[head]