# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightOnly = [] 

        q = deque([root])

        while q:
            # Adding children of inside nodes
            for i in range(len(q)-1):
                node = q.popleft()

                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
            # Right most node 
            node = q.popleft()
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                rightOnly.append(node.val)
            
        return rightOnly