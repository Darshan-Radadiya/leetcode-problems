class TrieNode:
    def __init__(self):
        self.childNode = {}
        self.wordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        currentNode = self.root

        for c in word:
            if c not in currentNode.childNode:
                currentNode.childNode[c] = TrieNode()
            currentNode = currentNode.childNode[c]
        currentNode.wordEnd = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            currentNode = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    for child in currentNode.childNode.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in currentNode.childNode:
                        return False
                    currentNode = currentNode.childNode[word[i]]
            return currentNode.wordEnd

        return dfs(0,self.root)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)