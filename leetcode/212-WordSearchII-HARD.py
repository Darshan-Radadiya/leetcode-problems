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


            