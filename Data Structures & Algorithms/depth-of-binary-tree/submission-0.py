# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return findMaxDepth(root, 1)

def findMaxDepth(root, depth):
    if not root:
        return depth - 1

    depthLeft = findMaxDepth(root.left, depth + 1)
    depthRight = findMaxDepth(root.right, depth + 1)

    return max(depthLeft, depthRight)
