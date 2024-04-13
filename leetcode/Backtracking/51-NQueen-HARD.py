class Solution:
    def totalNQueens(self, n: int) -> int:
        colSet = set()
        positiveSet = set()
        negativeSet = set()
        board = [["."] * n for row in range(n)]
        res = 0

        def backtrack(row):
            if row == n:
                nonlocal res
                res += 1
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
    
