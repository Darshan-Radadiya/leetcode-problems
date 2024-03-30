from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft = None, topRight = None, bottomLeft = None, bottomRight = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # check if all the values in the current grid is same.
        def allSame(grid, r, c, gridSize):
            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[r][c] != grid[r + i][c + j]:
                        return False
            return True
        
        # run the dfs on all four sides. 
        def dfs(grid, r, c, gridSize):
            if allSame(grid, r, c, gridSize):
                return Node(grid[r][c], True)
            else:
                root = Node(1, False)
                gridSize = gridSize // 2
                root.topLeft = dfs(grid, r, c, gridSize)
                root.topRight = dfs(grid, r, c + gridSize, gridSize)
                root.bottomLeft = dfs(grid, r + gridSize, c, gridSize)
                root.bottomRight = dfs(grid, r + gridSize, c + gridSize, gridSize)
            return root
        
        # start from the topLeft corner of the grid.
        return dfs(grid, 0, 0, len(grid))
    
print("Time Complexity is: O(n^2 log N)\n" )
print("Space Complexity is: O(log(n))")
