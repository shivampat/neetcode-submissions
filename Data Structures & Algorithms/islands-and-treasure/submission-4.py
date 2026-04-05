from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # We get the loc of every treasure chest
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2 ** 31 - 1

        q = deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))

        distance = 0 
        while q:
            for i in range(len(q)):
                x, y = q.popleft()

                if grid[x][y] == INF:
                    grid[x][y] = distance
                
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dx, dy in dirs:
                    if 0 <= x + dx < ROWS and 0 <= y + dy < COLS and grid[x + dx][y + dy] == INF:
                        q.append((x + dx, y + dy))
            distance += 1
        
                    

