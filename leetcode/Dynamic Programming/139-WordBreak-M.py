# Memoization Version
class Solution:
    def wordBreakMemoizationApproach(self, s: str, wordDict: list[str]) -> bool:
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

# Tabulation Approach
class Solution:
    def wordBreakTabulationApproach(self, s: str, wordDict: list[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for ic in range(len(s)):
            if dp[ic] == True:
                for word in wordDict:
                    if s[ic:len(word)+ic] == word:
                        dp[len(word)+ic] = True
        print(dp)
        return dp[len(s)]


sol = Solution()
# s = "leetcode"
# wordDict = ["leet","code"] // True
# s = "applepenapple"
# wordDict = ["apple","pen"] // True

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]   # False


# s = "abcdef"
# wordDict = ["ab","abc","cd","def","abcd"]

ExpectedOutput = False
# Output = sol.wordBreakMemoizationApproach(s,wordDict) 
Output1 = sol.wordBreakTabulationApproach(s,wordDict) 
# print("\nOutput of wordBreakMemoizationApproach:      ", Output ,"\n" )
print("\nOutput of wordBreakTabulationApproach:       ", Output1 ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
# print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output1, "\n" )
print("Time Complexity for Memo is: O(N(s)*m(wordDict len)*m(wordDict len))\n" )
print("Space Complexity for memo is: O(M^2)\n" )


print("Time Complexity for Tabulation is: O(N*m^2(wordDict len))\n" )
print("Space Complexity for Tabulation is: O(M)\n" )
