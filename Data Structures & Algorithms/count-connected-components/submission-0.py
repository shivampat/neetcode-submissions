class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for i in range(n)]

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set() 
        numComponents = 0
        for node in range(n):
            if node in visited:
                continue
            
            stack = [node]

            while stack:
                currNode = stack.pop()

                visited.add(currNode)

                for n in adjList[currNode]:
                    if n not in visited:
                        stack.append(n)
            
            numComponents += 1
        
        return numComponents
            

