from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque([])
        minutes = 0 

        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        
        # We run multi-source bfs now, but we also run our loop on both
        # the queue existing and if fresh > 0 to ensure that we stop our loop once
        # all fruits are rotten

        # in our loop, we dequeue all current rotten fruits
        # we will add their neighbors if their neighbors are in the grid and are fresh fruit
        # after dequeing, we will increment our minutes count

        while fresh > 0 and rotten:
            for _ in range(len(rotten)):
                i, j = rotten.popleft()

                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for di, dj in dirs:
                    if 0 <= i + di < ROWS and 0 <= j + dj < COLS and grid[i + di][j + dj] == 1:
                        grid[i + di][j + dj] = 2 
                        fresh -= 1
                        rotten.append((i+di, j+dj))

            
            minutes += 1

        return minutes if fresh == 0 else -1
                    
