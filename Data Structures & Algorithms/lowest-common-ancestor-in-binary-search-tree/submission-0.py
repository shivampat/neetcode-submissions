# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pTrace, qTrace = self.getTrace(root, p), self.getTrace(root, q)

        for i in range(min(len(pTrace), len(qTrace)) - 1, -1, -1):
            pnode, qnode = pTrace[i], qTrace[i]

            if pnode.val == qnode.val:
                return pnode
        
        return None


    def getTrace(self, root, node):
        val = node.val
        trace = []
        while True:
            trace.append(root)

            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                break
        
        return trace