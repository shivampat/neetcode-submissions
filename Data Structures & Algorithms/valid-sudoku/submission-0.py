class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i:set() for i in range(9)}
        col_map = {j:set() for j in range(9)}
        square_map = {(i,j):set() for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                row_set = row_map[i]
                col_set = col_map[j]
                square_set = square_map[(i // 3,j // 3)]
                if cell == ".":
                    continue
                
                if cell in row_set or \
                 cell in col_set or \
                 cell in square_set:
                    return False
                
                row_set.add(cell)
                col_set.add(cell)
                square_set.add(cell)
        return True

                


        

            

