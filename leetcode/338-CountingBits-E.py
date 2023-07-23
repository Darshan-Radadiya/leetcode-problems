class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

sol = Solution()
n = 5
ExpectedOutput = [0,1,1,2,1,2]
Output = sol.countBits(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n Log n)\n" )
