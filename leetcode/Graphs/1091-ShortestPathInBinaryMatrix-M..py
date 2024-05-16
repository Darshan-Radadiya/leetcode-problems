from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        q.append((0,0,1)) # row, col, currPathLen
        visited.add((0,0))
        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        while q:
            r, c, length = q.popleft()

            if min(r, c) < 0 or max(r, c) == len(grid) or grid[r][c] == 1:
                continue
            if r == len(grid) - 1 and c == len(grid) - 1:
                return length
            for dr, dc in directions:
                if (r + dr, c + dc) not in visited:
                    q.append((dr + r, dc + c, length + 1))
                    visited.add((dr+r, dc +c))
        return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
sol = Solution()
Output = sol.shortestPathBinaryMatrix(grid)
ExpectedOutput = 4
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N^2) and Space O(N)\n" )