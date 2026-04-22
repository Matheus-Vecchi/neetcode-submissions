class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        linhas = {}
        colunas = {}
        grid = {}

        for row in range(len(board)):
            for column in range(len(board)):
                if row not in linhas:
                    linhas[row] = []
                if column not in colunas:
                    colunas[column] = []
                linhas[row].append(board[row][column])
                colunas[column].append(board[row][column])

                if (row // 3, column // 3) not in grid:
                    grid[(row // 3, column // 3)] = []
                grid[(row // 3, column // 3)].append(board[row][column])
        
        for value in linhas.values():
            filtered = [x for x in value if x != "."]
            if len(filtered) != len(set(filtered)):
                return False
        
        for value in colunas.values():
            filtered = [x for x in value if x != "."]
            if len(filtered) != len(set(filtered)):
                return False
        
        for value in grid.values():
            filtered = [x for x in value if x != "."]
            if len(filtered) != len(set(filtered)):
                return False


        return True