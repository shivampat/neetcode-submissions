# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Solution:
        # Run bfs on both trees simultaneously
        # for each level, check the nodes for their values and if None etc. 
        # if they dont match return false
        # once all nodes are seen, return True

        q_p, q_q = deque([p]), deque([q])

        while q_p and q_q:
            if len(q_p) != len(q_q):
                return False
            
            for i in range(len(q_p)):
                p_node, q_node = q_p.popleft(), q_q.popleft()

                if not p_node and not q_node:
                    continue

                if not p_node or not q_node or p_node.val != q_node.val:
                    return False

                q_p.append(p_node.left)
                q_p.append(p_node.right)
                q_q.append(q_node.left)
                q_q.append(q_node.right)
        
        return len(q_p) == len(q_q)
