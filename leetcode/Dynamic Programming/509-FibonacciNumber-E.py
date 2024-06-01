class Solution:
    def fib(self, n: int) -> int:

        #  bottom up
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        # with memoization
        def solve(m):
            if m == 0 or m == 1:
                return m
            if memo[m] != -1:
                return memo[m]
            return solve(m-1) + solve(m-2)
        memo = [-1]* (n+1)
        return solve(n)

        # Time is 2^n - that's why we need memoization.   
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)


# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.