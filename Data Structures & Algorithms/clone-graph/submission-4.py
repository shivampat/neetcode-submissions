"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloneMap = {}
        cloneMap[node] = Node(val=node.val)
        q = deque([node])

        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in cloneMap:
                    q.append(n)
                    cloneMap[n] = Node(val=n.val)
                cloneMap[curr].neighbors.append(cloneMap[n])
        
        return cloneMap[node]