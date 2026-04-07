class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Initial solution: we can iteratively search for the first letter in the grid.
        If we find it, we can run dfs at that location, searching neighboring tiles for 
        the next letter in the word. If we eventually reach the last letter of word, we 
        return true. Otherwise, move on to the next location of the start of the word.
        If we reach the end, return False

        the dfs function will use a set to track visited cells to prevent repeats of cells.

        Time complexity: O(m * n), where m is num of rows and n is num of cols
        Space complexity: O(w) where w is the length of word
        """ 
        if not word:
            return False

        ROWS, COLS = len(board), len(board[0])

        visited = set()
        def dfs(indx, i, j):
            if indx == len(word):
                return True

            if i < 0 or i >= ROWS or j < 0 or j >= COLS \
            or board[i][j] != word[indx] or (i,j) in visited:
                return False
            
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            seen = False

            visited.add((i,j))
            for di, dj in dirs:
                if seen:
                    break
                
                seen = dfs(indx + 1, i + di, j + dj)
            visited.remove((i,j))
            
            return seen

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(0, i, j):
                    return True
        
        return False
