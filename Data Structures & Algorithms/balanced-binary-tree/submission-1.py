# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        LRHts = {None: 0}
        stack = [root]

        while stack:
            node = stack[-1]

            if node and node.left and node.left not in LRHts:
                stack.append(node.left)
            elif node and node.right and node.right not in LRHts:
                stack.append(node.right)
            else:
                stack.pop()

                leftHeight, rightHeight = LRHts[node.left], LRHts[node.right]

                if abs(leftHeight - rightHeight) > 1:
                    return False
                
                LRHts[node] = max(leftHeight, rightHeight) + 1

        return True
