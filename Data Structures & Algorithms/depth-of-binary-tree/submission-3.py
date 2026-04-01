# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs 
        if not root:
            return 0

        q = deque([root])
        heights = {root:1}

        while q:
            currNode = q.popleft()

            if currNode.left:
                q.append(currNode.left)
                heights[currNode.left] = heights[currNode] + 1
            if currNode.right:
                q.append(currNode.right)
                heights[currNode.right] = heights[currNode] + 1
        
        return max(heights.values())
            

