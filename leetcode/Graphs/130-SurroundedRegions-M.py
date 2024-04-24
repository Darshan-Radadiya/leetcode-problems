from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROW, COL = len(board), len(board[0])
        def explore(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or board[r][c] != "O":
                return 
            board[r][c] = "T"
            explore(r - 1, c)
            explore(r + 1, c)
            explore(r, c - 1)
            explore(r, c + 1)
            return
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O" and (r in [0, ROW-1] or c in [0, COL-1]):
                    explore(r,c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "T":
                    board[r][c] = "O"

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
ExpectedOutput = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Output = sol.solve(board) 
print("\nOutput is:      ", board ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == board, "\n" )
print("Time Complexity is: O(ROWS*COLS)\n" )
