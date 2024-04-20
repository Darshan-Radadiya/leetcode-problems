class Solution:
    def pacificAtlantic(self, heights):

        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, prevHeight, visited):
            # we are following reverse logic here if the current cell has higher value than previous
            # then we will add that cell
            # because we are moving from ocean to corresponding cell.
            if (r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                (r,c) in visited or
                heights[r][c] < prevHeight):
                return 
            visited.add((r,c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)

        # Visiting first and last row.
        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS-1, c, heights[ROWS-1][c],atlantic)

        #visiting first and last column.
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS-1, heights[r][COLS-1],atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res


sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
ExpectedOutput = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Output = sol.pacificAtlantic(heights) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(ROWS*COLS)\n" )
