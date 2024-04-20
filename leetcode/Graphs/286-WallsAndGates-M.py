# 286. Walls and Gates
# Description
# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
# Leetcode premium question - https://leetcode.ca/2016-09-11-286-Walls-and-Gates/

from typing import List
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWs, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        for r in range(ROWs):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c,0])
                    visited.add((r,c))
        
        while q:
            r, c, distance = q.popleft()
            for dr, dc in ([-1,0], [1,0], [0,-1], [0,1]):
                row, col = dr + r, dc + c
                if row >= 0 and row < ROWs and col >= 0 and col < COLS and (row,col) not in visited and rooms[row][col] != -1:
                    visited.add((row,col))
                    rooms[row][col] = distance + 1
                    q.append([row,col, distance + 1])
        return rooms


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
sol = Solution()
Output = sol.wallsAndGates(rooms)
ExpectedOutput =  [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )