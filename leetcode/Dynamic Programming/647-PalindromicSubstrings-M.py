class Solution:
    # Brute force using DP O(n^2): Exceed TLE for Python....
    def countSubstrings(self, s: str) -> int:
        def checkIsPalindrome(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            original_i, original_j = i, j
            while i < j:
                if s[i] != s[j]:
                    memo[original_i][original_j] = 0
                    return memo[original_i][original_j]
                else:
                    i += 1
                    j -= 1
            memo[original_i][original_j] = 1
            return memo[original_i][original_j]
    
        count = 0
        n = len(s)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                if checkIsPalindrome(i, j) == 1:
                    count += 1
        
        return count
        
    # Bottom up approach - passes on LC - O(n^2)
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False for i in range(n)] for i in range(n)]
        for L in range(1,n+1):
            i = 0
            while i + L - 1 < n:
                j = i + L - 1
                if  i == j:
                    dp[i][j] = True
                elif i+1 == j:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False
                if dp[i][j]:
                    res += 1
                i += 1
        return res

    #  optimized way O(n^2)
    def checkPalindrome(self,s,l,r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    def countSubstrings(self, s: str) -> int:
        palindromeStrCount = 0

        for i in range(len(s)):
            #odd length
            palindromeStrCount += self.checkPalindrome(s,i,i)
                
            #Even length
            palindromeStrCount += self.checkPalindrome(s,i,i+1)

        return palindromeStrCount

sol = Solution()
s = "aaa"
ExpectedOutput = 6
Output = sol.countSubstrings(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n*n) or O(n^2)\n" )
