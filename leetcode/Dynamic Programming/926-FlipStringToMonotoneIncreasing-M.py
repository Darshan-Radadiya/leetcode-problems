class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #  OPTIMAL WAY
        #  Time Complexity: O(n)
        #  Space Complexity: O(1)

        flips = 0
        countOfOne = 0
        for currDigit in  s:
            if currDigit == '1':
                countOfOne += 1
            else:
                flips = min( 1 + flips, countOfOne)
        return flips

        #  TOP DOWN DP
        #  Time Complexity: O(n)
        #  Space Complexity: O(n)
        def solve(i, prevVal):
            if i == n:
                return 0
            
            if dp[i][prevVal] != -1:
                return dp[i][prevVal]

            flip = float('inf')
            noFlip = float('inf')
            
            # if curr digit is 0
            if s[i] == '0':
                if prevVal == 0:
                    flip = 1 + solve(i+1, 1)  # flip 0 to 1
                    noFlip = solve(i+1, 0)    # keep 0
                else:
                    flip = 1 + solve(i+1, 1)  # flip 0 to 1

            # if curr digit is 1
            else:
                if prevVal == 0:
                    flip = 1 + solve(i+1, 0)  # flip 1 to 0 (not useful)
                    noFlip = solve(i+1, 1)    # keep 1
                else:
                    noFlip = solve(i+1, 1)    # keep 1
            
            dp[i][prevVal] = min(flip, noFlip)
            return dp[i][prevVal]

        n = len(s)
        if n == 1:
            return 0
        dp = [[-1 for _ in range(2)] for _ in range(n+1)]
        return solve(0, 0)

sol = Solution()
s = "100000001010000"
ExpectedOutput = 3
Output = sol.minFlipsMonoIncr(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
