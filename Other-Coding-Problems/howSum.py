# give array and number find the combination of number that can add up to given number.
# return combination values in array.
# O(m^2*n) - time 
# O(m^2) - space

def howSum(target,nums):
    dp = [None]*(target+1)
    dp[0] = []
    for i in range(target):
        if dp[i] or dp[i] == []:
            for num in nums:
                if i+num <= target:
                    newArr = dp[i] + [num]
                    dp[i+num] = newArr
    return dp[target]


print(howSum(7,[5,4,3,7]))
print(howSum(7,[2,4]))
print(howSum(100,[3,4,25]))
print(howSum(300,[7,14]))