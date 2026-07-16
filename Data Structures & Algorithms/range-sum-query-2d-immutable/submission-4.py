class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = {}
        acc = 0

        for row in range(len(matrix)):
            acc = 0
            for col in range(len(matrix[row])):
                if row > 0:
                    acc += matrix[row][col] + self.prefix[row-1][col]
                else:
                    acc += matrix[row][col]
                
                if row not in self.prefix:
                    self.prefix[row] = [acc]
                else:
                    self.prefix[row].append(acc)
                
                if row > 0:
                    acc -= self.prefix[row-1][col]
                
                
                    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        
        if row1 == 0 and col1 == 0:
            return total
        
        if row1 == 0:
            left_diff = self.prefix[row2][col1-1]
            return total - left_diff
        
        if col1 == 0:
            upper_diff = self.prefix[row1-1][col2]
            return total - upper_diff
        
        upper_diff = self.prefix[row1-1][col2]
        left_diff = self.prefix[row2][col1-1] - self.prefix[row1-1][col1-1]

        return total - (upper_diff + left_diff)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)