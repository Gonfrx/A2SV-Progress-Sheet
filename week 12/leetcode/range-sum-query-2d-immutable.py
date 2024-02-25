class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in range(len(matrix)):
            temp = []
            for col in range(len(matrix[0])):
                if row == 0 and col == 0: 
                    temp.append(matrix[row][col])
                elif row == 0: 
                     temp.append(temp[col-1] + matrix[row][col])
                elif col == 0: 
                    temp.append(self.prefix[row-1][col] + matrix[row][col])
                else:
                    temp.append(self.prefix[row-1][col] + temp[col-1] + matrix[row][col] - self.prefix[row-1][col-1])
            self.prefix.append(temp)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #[row1 - 1][col2] + [row2][col1-1]  - [row1-1][col1-1]
        #first case both row1 and col1 are 0,0,
        if row1 == 0 and col1 == 0: 
            return self.prefix[row2][col2] 
        #second case row1 is 0: 
        elif row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1] 
        #second case with col1 is 0: 
        elif col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        #both are not 0:
        else: 
            return self.prefix[row2][col2] - (self.prefix[row1-1][col2] + self.prefix[row2][col1-1] ) + self.prefix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)