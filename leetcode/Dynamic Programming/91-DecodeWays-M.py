class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
               res += dfs(i+2)
            
            dp[i] = res
            return res

        return dfs(0)

sol = Solution()
s = "12"
ExpectedOutput = 2 # Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Output = sol.countSubstrings(s)

print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
