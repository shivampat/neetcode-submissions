class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = [] 
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        for j in range(COLS):
            if board[0][j] == 'O':
                stack.append((0,j))
            if board[ROWS-1][j] == 'O':
                stack.append((ROWS-1,j))
        
        for i in range(1, ROWS-1):
            if board[i][0] == 'O':
                stack.append((i,0))
            if board[i][COLS-1] == 'O':
                stack.append((i,COLS-1))
        
        while stack:
            i, j = stack.pop()

            if i < 0 or i >= ROWS or j < 0 or j >= COLS \
            or (i,j) in visited or board[i][j] == 'X':
                continue
            
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))

            visited.add((i,j))
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited:
                    board[i][j] = 'X'