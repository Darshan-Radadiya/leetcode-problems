# complexity is O(2n).

def feb_without_memo(n):
    if n <= 2:
        return 1
    return feb_without_memo(n-1) + feb_without_memo(n-2)
# print(feb(2))
# print(feb(5))
# print(feb(50)) # it is going to take much more time

# with the use of memoization
# we can do it in O(n) time and space.
# that is much more efficient

# Memoization approach

def fibonacciWithMemo(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fibonacciWithMemo(n-1,memo) + fibonacciWithMemo(n-2,memo)
    return memo[n]

print("\tfeb_with_memo    \t", fibonacciWithMemo(50,{}))

# Tabulation Approach

def fibonacciWithTabulation(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return (dp[n])

print("\tfeb_with_Tabulation\t", fibonacciWithTabulation(50))
