class TrieNode():
    def __init__(self):
        self.childNode = {}
        self.isWord = False
    
    def addWord(self,word):
        currentNode = self
        for c in word:
            if c not in currentNode.childNode:
                currentNode.childNode[c] = TrieNode()
            currentNode = currentNode.childNode[c]
        currentNode.isWord = True 

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROW, COL = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r,c,node,word):
            if (r < 0 or
                c < 0 or
                r == ROW or
                c == COL or
                (r,c) in visited or
                board[r][c] not in node.childNode):
                return 
            
            visited.add((r,c))
            node = node.childNode[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,root,"")

        return list(res)

sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
ExpectedOutput = ["eat","oath"]
Output = sol.findWords(board, words) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is:  O(m * L + n * L) m is the number of words in the words list. L is the average length of words. n is the total number of cells in the board (ROW * COL).\n" )
