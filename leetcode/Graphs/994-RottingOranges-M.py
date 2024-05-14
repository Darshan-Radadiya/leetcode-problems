from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        totalMin = 0
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        # Multi source BFS  
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ([[1,0], [-1, 0], [0, 1], [0, -1]]):
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                        continue
                    q.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1                

            totalMin += 1

        return totalMin if fresh == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution()
Output = sol.orangesRotting(grid)
ExpectedOutput = 4
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )