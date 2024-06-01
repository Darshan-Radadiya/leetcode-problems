from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def explore(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid2[r][c] == 0:
                return True
            visited.add((r, c))
            up = explore(r - 1, c)
            down = explore(r + 1, c)
            left = explore(r, c - 1)
            right = explore(r, c + 1)
            return grid1[r][c] == 1 and up and down and left and right

        ROWS = len(grid1)
        COLS = len(grid1[0])
        res = 0
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r,c) not in visited and explore(r, c):
                    res += 1
        return res

    
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
sol = Solution()
Output = sol.countSubIslands(grid1, grid2)
ExpectedOutput = 3
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )