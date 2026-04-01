# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = 0
        stack = [root]
        htDiam = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node and node.left and node.left not in htDiam:
                stack.append(node.left)
            elif node and node.right and node.right not in htDiam:
                stack.append(node.right)
            else:
                stack.pop()

                leftHeight, leftDiam = htDiam[node.left]
                rightHeight, rightDiam = htDiam[node.right]

                newHeight = max(leftHeight, rightHeight) + 1
                newDiam = max(leftDiam, rightDiam, leftHeight + rightHeight)

                length = max(length, newDiam)

                htDiam[node] = (newHeight, newDiam)
        
        return length