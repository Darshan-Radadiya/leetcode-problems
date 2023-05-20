class Solution:
    def pacificAtlantic(heights):
        return ""



sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
ExpectedOutput = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Output = sol.pacificAtlantic(heights) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(ROWS*COLS)\n" )
