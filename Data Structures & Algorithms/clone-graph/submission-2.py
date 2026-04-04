from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        nodeMap = {None:None}

        queue = deque([node])
        nodeMap[node] = Node(val=node.val)

        while queue:
            curr = queue.popleft()

            for n in curr.neighbors:
                if n not in nodeMap:
                    nodeMap[n] = Node(val=n.val)
                    queue.append(n)
                nodeMap[curr].neighbors.append(nodeMap[n])
        
        return nodeMap[node]