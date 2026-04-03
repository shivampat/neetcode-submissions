class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0

        def dfs(i, j):
            nonlocal grid

            if i >= ROWS or i < 0 or j >= COLS or j < 0 or grid[i][j] == '0':
                return

            if grid[i][j] == '1':
                grid[i][j] = '0'
            
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    numIslands += 1
        

        return numIslands