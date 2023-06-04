# give array and number find the combination of number that can add up to given number.
# return boolean value.
# O(m*n) - time 
# O(m) - space

def canSum(target,nums):
    dp = [False]*(target+1)
    dp[0] = True
    for i in range(target):
        if dp[i]:
            for num in nums:
                if i+num <= target: dp[i+num] = True

    return dp[target]


print(canSum(7,[5,4]))
print(canSum(100,[3,4]))