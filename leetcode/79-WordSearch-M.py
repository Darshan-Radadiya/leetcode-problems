class Solution:
    def exist(self, board, word):
        
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
                
            if (c < 0 or
            r < 0 or
            r >= ROWS or
            c >= COLS or
            (r,c) in path or
            word[i] != board[r][c]):
                return False
            
            path.add((r,c))
            res = (
                    dfs(r-1, c, i+1) or
                    dfs(r+1, c, i+1) or
                    dfs(r, c-1, i+1) or
                    dfs(r, c+1, i+1)
            )
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
Output = True
sol = Solution()
print("Expected Output:", Output)
print("Output: ",sol.exist(board,word))
   
   
# O(n * m * dfs)
# O( n * m * 4*wordLen) = 4 bcs we r calling dfs 4 time.