from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        # Create a DP table initialized with infinity
        dp = [[float('inf')] * cols for _ in range(rows)]
        
        # Initialize the last row of DP table with the values of the last row of the matrix
        for c in range(cols):
            dp[rows - 1][c] = matrix[rows - 1][c]
        
        # Fill the DP table from bottom to top
        for r in range(rows - 2, -1, -1):
            for c in range(cols):
                # Current element value
                currEle = matrix[r][c]
                
                # Possible moves
                left = dp[r + 1][c - 1] if c - 1 >= 0 else float('inf')
                down = dp[r + 1][c]
                right = dp[r + 1][c + 1] if c + 1 < cols else float('inf')
                
                # Minimum falling path sum for the current cell
                dp[r][c] = currEle + min(left, down, right)
        
        # The result is the minimum value in the first row of the DP table
        return min(dp[0])


sol = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
ExpectedOutput = 13
Output = sol.minFallingPathSum(matrix) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(row * col)\n" )
