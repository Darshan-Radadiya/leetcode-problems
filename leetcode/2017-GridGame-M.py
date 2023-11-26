class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:

        prefixSum = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]
        prefixSum[0][0] = grid[0][0] 
        prefixSum[1][0] = grid[1][0]
        for row in range(len(grid)):
            for j in range(1, len(grid[row])):
                prefixSum[row][j] = prefixSum[row][j - 1] + grid[row][j]

        res, currMax = float('inf'), 0
        for j in range(len(grid[0])):
            top = prefixSum[0][-1] - prefixSum[0][j]
            bottom = prefixSum[1][j -1] if j > 0 else 0
            currMax = max(top, bottom)
            res = min(currMax, res)

        return res

sol = Solution()
grid = [[1,3,1,15],[1,3,3,1]]
ExpectedOutput = 7
Output = sol.gridGame(grid) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )
