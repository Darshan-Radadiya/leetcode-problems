class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        print("1st time",matrix)

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        print("2nd time",matrix)
        
        # zero out the first column of the matrix.
        if matrix[0][0] == 0:
            for r in range(ROWS):   
                matrix[r][0] = 0
        print("3rd time",matrix)

        # zero out the first row if we need to.
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        print("4th time",matrix)

        return matrix

sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 1 1 1     ==      1 0 1       ==         1 0 1    ==  1 0 1   ==  1 0 1   
# 1 0 1     ==      0 0 1       ==         0 0 0    ==  0 0 0   ==  0 0 0
# 1 1 1     ==      1 1 1       ==         1 0 1    ==  1 0 1   ==  1 0 1
ExpectedOutput = [[1,0,1],[0,0,0],[1,0,1]]
Output = sol.setZeroes(matrix) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m*n) and Space is O(1)\n" )