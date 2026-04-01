# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # assume root will never be null
        stack = [(root, root.val)]
        numGoodNodes = 0

        visited = set([None])

        while stack:
            node, maxValSeen = stack[-1]

            newMax = max(maxValSeen, node.val)

            if node.left not in visited:
                stack.append((node.left, newMax))
                visited.add(node.left)
            elif node.right not in visited:
                stack.append((node.right, newMax))
                visited.add(node.right)
            else:
                if node.val >= maxValSeen:
                    numGoodNodes += 1
                stack.pop()
            
        return numGoodNodes

            
            

