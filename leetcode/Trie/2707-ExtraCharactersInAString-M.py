from typing import List

# Bottom Up Dynamic Programming
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)
        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]
    
# Top down DP O(N^3)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {}
        words = set(dictionary)
        def dfs(i):
            if i == len(s):
                return 0
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1) 
            
            for j in range(i, len(s)):
                if s[i: j+1] in words:
                    res = min(res, dfs(j+1))
            dp[i] = res
            return res
        return dfs(0)

# Bottom Up Trie + DP
# Time complexity: O(N2+M⋅K) n = len(s), m = len(str(dict)), k = len(dict)
class TrieNode():
    def __init__(self):
        self.childNode = {}
        self.isWord = False
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
       
        root = TrieNode()
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr.childNode:
                    curr.childNode[c] = TrieNode()
                curr = curr.childNode[c]
            curr.isWord = True
        dp = [0]* (len(s)+1)
        for start in range(len(s) - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            curr = root     
            for end in range(start, len(s)):
                if s[end] in curr.childNode:
                    curr = curr.childNode[s[end]]
                    if curr.isWord:
                        dp[start] = min(dp[start], dp[end+1])
                else:
                    break
        return dp[0]

# Top down Trie + DP
# Time complexity: O(N2+M⋅K) n = len(s), m = len(str(dict)), k = len(dict)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr.childNode:
                    curr.childNode[c] = TrieNode()
                curr = curr.childNode[c]
            curr.isWord = True

        dp = {}
        def dfs(i):
            if i == len(s):
                return 0
            if i in dp:
                return dp[i]
            curr = root
            res = 1 + dfs(i + 1) 
            
            for j in range(i, len(s)):
                if s[j] not in curr.childNode:
                    break
                curr = curr.childNode[s[j]]
                if curr.isWord:
                    res = min(res, dfs(j+1))

            dp[i] = res
            return res
        return dfs(0)
            
        
sol = Solution()
s = "leetscode"
dictionary = ["leet","code","leetcode"]
ExpectedOutput = 1
Output = sol.minExtraChar(s, dictionary) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity for DP solution is: O(n^3) and DP+ Trie is O(N^2 + M * K)\n" )
