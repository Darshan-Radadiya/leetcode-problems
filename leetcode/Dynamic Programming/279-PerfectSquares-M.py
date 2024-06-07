class Solution:
    def numSquares(self, n: int) -> int:
        def solve(m):
            if m == 0:
                return 0

            if memo[m] != -1:
                return memo[m]
            i = 1
            minCount = float("inf")
            while i*i <= m:
                res = 1+solve(m - i*i)
                minCount = min(minCount, res)
                i += 1
            memo[m] = minCount
            return memo[m]
        memo = [-1 for i in range(n+1)]

        return solve(n)
 
sol = Solution()
n = 15
ExpectedOutput = 4
Output = sol.numSquares(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^(3/2))\n" )
