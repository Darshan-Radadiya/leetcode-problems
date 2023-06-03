# in this problem we have m*n grid 
# in which traveler can only go down or right 
# our task is to find number of ways we can reach the top left to bottom right
# with brute force complexity is O(2^m+n)
# but with use of memo we can bring it to O(m*n)
# space for both case is O(m+n)

# Memoization approach

def travelerWithMemo(row,col,memo):
    
    key = str(row) + "," + str(col)
    if key in memo:
        return memo[key]
    if row == 0 or col == 0:
        return 0
    if row == 1 or col == 1:
        return 1
    memo[key] = travelerWithMemo(row-1,col,memo) + travelerWithMemo(row,col-1,memo)
    return memo[key]    
print("\tMemoization approach \t", travelerWithMemo(18,18,{}))


# Tabulation Approach
def travelerWithTabulation(m,n):
    dp = [[0] * n for _ in range(m)]

    for R in range(m):
        for C in range(n):
            if R == 0 or C == 0:
                dp[R][C] = 1
            else:
                dp[R][C] = dp[R-1][C] + dp[R][C-1]

    return dp[m-1][n-1]

    # Time = O(n * m) space =  O(m*n)

print("\tTabulation approach \t", travelerWithTabulation(18,18))
print("\tTabulation approach \t", travelerWithTabulation(2,3))
print("\tTabulation approach \t", travelerWithTabulation(3,7))
