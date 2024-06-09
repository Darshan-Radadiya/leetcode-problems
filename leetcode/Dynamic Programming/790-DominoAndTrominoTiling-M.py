class Solution:
    def numTilings(self, n: int) -> int:
        # Its based on the mathematical derivation
        # Don't expect you can solve it on your own on the first go..
        #  See notes for better clarity... 
        #  Bottom up O(n)
        if n == 2 or n == 1:
            return n
        dp = [-1]*(n+1)
        MOD = 1_000_000_007
        
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD

        return dp[n]

        #  TOP DOWN O(n)
        dp = [-1]*(n+1)
        MOD = 1_000_000_007
        def solve(m):
            if m <= 2:
                return m
            if m == 3:
                return 5
            
            if dp[m] != -1:
                return dp[m]
            
            dp[m] = ((solve(m-1) * 2) % MOD + (solve(m - 3)) % MOD) %  MOD
            return dp[m]

        return solve(n)

sol = Solution()
n = 4
ExpectedOutput = 11
Output = sol.numTilings(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
