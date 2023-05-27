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

def feb_with_memo(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = feb_with_memo(n-1,memo) + feb_with_memo(n-2,memo)
    return memo[n]

print("feb_with_memo", feb_with_memo(50,{}))
 
