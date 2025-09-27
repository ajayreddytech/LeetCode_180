# prefix matrix = inside PM, i+1, j+1 th element = sum of all the eles in the sub matrix from 0,0 to i,j
# sum from prefix matrix = (outerRectangle) - (sideRectanngle1) - (sideRectangle2) + (add double deducted rectange area)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix # given matrix
        self.prefix = self.getPrefix(matrix) # the prefix matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        return sum

    def getPrefix(self, matrix: List[List[int]]):
        r = len(matrix) # no. of rows
        c = len(matrix[0]) # no. of columns
        prefix = [[0]*(c+1) for i in range(r+1)] #initializing zero matrix of r+1 and c+1

        # nested loop ??
        # we need this nested loop at any cost, 
        # but the good thing is, we need it only once
        # we will use this inside the constructor to get the prefix matrix 
        # and thats it, we will never use this nested loop again
        for i in range(r):
            for j in range(c):
                prefix[i+1][j+1] = matrix[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]

        return prefix


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)