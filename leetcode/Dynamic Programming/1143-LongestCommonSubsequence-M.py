class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                if text2[j-1] == text1[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    #   If you want to print the LCS
        i, j = M, N
     
        lcs = ""
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                lcs += text1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        print("Longest common subsequence is...",lcs[::-1])

        return dp[M][N]
    

        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]
        
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if text2[j] == text1[i]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]



sol = Solution()
text1 = "abcde"
text2 = "ace" 
ExpectedOutput = 3  
Output = sol.longestCommonSubsequence(text1,text2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(n * m)\n" )
