from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #  BOTTOM UP
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        #  Fill the first row where we can go right only bcs we can't come to this position from down.
        prevVal = 0
        for c in range(cols):
            dp[0][c] = prevVal + grid[0][c]
            prevVal = dp[0][c]
        
        #  Fill the first col where we can go down only bcs we can't come to this position from right.
        prevVal = 0
        for r in range(rows):
            dp[r][0] = prevVal + grid[r][0]
            prevVal = dp[r][0]
        
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = grid[r][c] + min(dp[r][c-1], dp[r-1][c])
        return dp[rows-1][cols-1]
    
        #  TOP DOWN 
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]

        def solve(i, j):
            #  if we reach the bottom right corner.
            if i == rows - 1 and j == cols - 1:
                dp[i][j] = grid[i][j]
                return dp[i][j]
            
            #  check wif we already calculated this value.
            if dp[i][j] != -1:
                return dp[i][j]

            # if we reach the last col then we can only go down.
            if j == cols - 1:
                dp[i][j] = grid[i][j] + solve(i+1, j)
                return dp[i][j]
            
            # if we reach the last row then we can only go right.
            elif i == rows - 1:
                dp[i][j] = grid[i][j] + solve(i, j+1)
                return dp[i][j]

            # we can go right or down and will consider the minimum of these two.
            else:
                dp[i][j] = min((grid[i][j] + solve(i, j+1)), (grid[i][j] + solve(i + 1, j))) 

            return dp[i][j]
        
        return solve(0,0)

sol = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
ExpectedOutput = 19
Output = sol.minPathSum(matrix) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(row * col)\n" )
