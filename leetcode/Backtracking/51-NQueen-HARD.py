from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        positiveSet = set()
        negativeSet = set()
        board = [["."] * n for row in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                currBoard = ["".join(r) for r in board]
                res.append(currBoard)
                return 
            
            for col in range(n):
                if col not in colSet and (row+col) not in positiveSet and (row-col) not in negativeSet:
                    board[row][col] = "Q"
                    colSet.add(col)
                    positiveSet.add((row+col))
                    negativeSet.add((row-col))

                    backtrack(row+1)

                    board[row][col] = "."
                    colSet.remove(col)
                    positiveSet.remove((row+col))
                    negativeSet.remove((row-col))
        backtrack(0)
        return res

    
n = 4
sol = Solution()
Output = sol.solveNQueens(n)
ExpectedOutput = [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']] 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n!)\n" )

