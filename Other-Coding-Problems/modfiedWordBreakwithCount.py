class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def canConstruct(s,wordDict,memo):
            if s in memo: return memo[s]
            if s == "": return 1
            count = 0
            for word in wordDict:
                prefix = s[:len(word)]
                if prefix == word:
                    suffix = s[len(prefix):]
                    tempCount = canConstruct(suffix,wordDict,memo) 
                    count += tempCount
            memo[s] = count            
            return count
        return canConstruct(s,wordDict,{})

sol = Solution()
# s = "leetcode"
# wordDict = ["leet","code"]
s = "applepenapple"
wordDict = ["apple","pen"]

ExpectedOutput = True
Output = sol.wordBreak(s,wordDict) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N(s)*m(wordDict len)*m(wordDict len))\n" )
print("Space Complexity is: O(M^2)\n" )
