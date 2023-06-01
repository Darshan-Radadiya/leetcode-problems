class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def canConstruct(s,wordDict,memo):
            if s in memo: return memo[s]
            if s == "": 
                count += 1
                return True
            for word in wordDict:
                prefix = s[:len(word)]
                if prefix == word:
                    suffix = s[len(prefix):]
                    if (canConstruct(suffix,wordDict,memo)): 
                        memo[s] = True
                        return True
            memo[s] = False            
            return False
        return canConstruct(s,wordDict,{})

sol = Solution()
# s = "leetcode"
# wordDict = ["leet","code"]
# s = "applepenapple"
# wordDict = ["apple","pen"]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

ExpectedOutput = False
Output = sol.wordBreak(s,wordDict) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N(s)*m(wordDict len)*m(wordDict len))\n" )
print("Space Complexity is: O(M^2)\n" )
