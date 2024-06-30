class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Bottom up O(m*n)
        M, N = len(str1), len(str2)
        dp = [[ 0 for _ in range(N + 1)]  for _ in range(M + 1)]

        for i in range(M+1):
            for j in range(N+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1])


        i, j = M, N
        SCS = ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                SCS += str1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] < dp[i][j-1]:
                    SCS += str1[i-1]
                    i -= 1
                else:
                    SCS += str2[j-1]
                    j -= 1
        while i > 0:
            SCS += str1[i-1]
            i -= 1

        while j > 0:
            SCS += str2[j-1]
            j -= 1

        return SCS[::-1]


sol = Solution()
text1 = "abac"
text2 = "cab" 
ExpectedOutput = "cabac"
Output = sol.shortestCommonSupersequence(text1,text2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(n * m)\n" )