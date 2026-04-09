class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adjList = {i:[] for i in range(n)} 
        for n1, n2 in edges:
            adjList[n2].append(n1)
            adjList[n1].append(n2)


        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for n in adjList[node]:
                if n == prev:
                    continue

                if not dfs(n, node):
                    return False
            
            return True

        return dfs(0, None) and len(visited) == n 



