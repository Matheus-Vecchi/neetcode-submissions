class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        linhas = {}
        colunas = {}
        grid = {}

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    pass
                else:
                    if row not in linhas:
                        linhas[row] = []
                    if col not in colunas:
                        colunas[col] = []
                    linhas[row].append(board[row][col])
                    colunas[col].append(board[row][col])
                    
                    if (row // 3, col // 3) not in grid:
                        grid[(row // 3, col // 3)] = []
                    grid[(row // 3, col // 3)].append(board[row][col])
    
        for array in linhas.values():
            setmap = set(array)
            if len(setmap) != len(array):
                return False
        
        for array in colunas.values():
            setmap = set(array)
            if len(setmap) != len(array):
                return False
        
        for array in grid.values():
            setmap = set(array)
            if len(setmap) != len(array):
                return False

        return True