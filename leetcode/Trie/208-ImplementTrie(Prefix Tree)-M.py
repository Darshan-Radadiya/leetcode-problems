class TrieNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.wordCount = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        currentNode = self.root

        for c in word:
            if not currentNode.childNode[ord(c) - ord('a')]:
                newNode = TrieNode()
                currentNode.childNode[ord(c) - ord('a')] = newNode
            currentNode = currentNode.childNode[ord(c) - ord('a')]
        currentNode.wordCount += 1
        return None

    def search(self, word: str) -> bool:
        currentNode = self.root
        for c in word:
            if not currentNode.childNode[ord(c) - ord('a')]:
                return False
            currentNode = currentNode.childNode[ord(c) - ord('a')]

        return currentNode.wordCount > 0


    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for c in prefix:
            if not currentNode.childNode[ord(c) - ord('a')]:
                return False
            currentNode = currentNode.childNode[ord(c) - ord('a')]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)