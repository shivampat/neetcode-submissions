class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or \
            j < 0 or j >= COLS or \
            grid[i][j] == 0:
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = 0
            
            down = dfs(i + 1, j)
            up = dfs(i - 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return down + up + left + right + 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    currArea = dfs(i,j)
                    maxArea = max(maxArea, currArea)
        
        return maxArea
