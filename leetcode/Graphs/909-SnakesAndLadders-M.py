from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def getCoordinates(num):
            rowFromTop = (num - 1) // n
            rowFromBottom = (n - 1) - rowFromTop
            col = (num-1) % n
            if (rowFromBottom % 2 != 0 and n % 2 != 0) or (rowFromBottom % 2 == 0 and n % 2 == 0):
                col = (n-1) - col 
            return [rowFromBottom, col]


        q = deque()
        visited = set()
        moves = 0
        q.append(1)
        visited.add(1)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == n*n:
                    return moves
                for i in range(1,7):
                    nextt = curr + i
                    if nextt <= n*n:
                        r, c = getCoordinates(nextt)
                        if board[r][c] != -1:
                            nextt = board[r][c]
                        if nextt not in visited:
                            q.append(nextt)
                            visited.add(nextt)
            moves += 1
        return -1                    

board = [[-1,-1,-1,9,-1,-1],[-1,-1,10,7,-1,-1],[-1,-1,-1,-1,-1,20],[-1,14,-1,-1,15,20],[31,29,-1,-1,7,36],[-1,-1,-1,13,18,5]]
sol = Solution()
Output = sol.snakesAndLadders(board)
ExpectedOutput = 1
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(M * N)\n" ) 