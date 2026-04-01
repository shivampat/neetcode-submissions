# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        while len(q) > 0:
            # Add children to queue 
            currnode = q.popleft()

            if currnode:
                q.append(currnode.left)
                q.append(currnode.right)
                currnode.left, currnode.right = currnode.right, currnode.left
        
        return root