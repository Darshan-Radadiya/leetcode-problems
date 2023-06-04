# give array and number find the combination of number that can add up to given number with minimum combinations.
# O(m*n)

# Memoization approach
def bestSum(targetSum,nums,memo):
    
    if memo is None:
        memo = {}

    if targetSum in memo: return memo[targetSum]

    if targetSum == 0: return []

    if targetSum < 0: return None

    shortCombination, combinations = None, []


    for n in nums:
        reminder = targetSum - n
        reminderCombinations = bestSum(reminder, nums, memo)
        if reminderCombinations != None:
            combinations = reminderCombinations + [n]
            if combinations != None or len(combinations) < len(shortCombination):
                shortCombination = combinations

    memo[targetSum] = shortCombination
    return shortCombination

print("\tMemoization approach of best sum   7",bestSum(7,[5,3,4,7],{}))
print("\tMemoization approach of best sum   8",bestSum(8,[2,5,3],{}))
print("\tMemoization approach of best sum 100",bestSum(100,[3,4,25],{}))


# Tabulation Approach
# Time = O(m^2*n)
# Space = O(m^2)
def bestSumTabulation(target, nums):
    dp = [None]*(target+1)
    dp[0] = []
    for i in range(target+1):
        if dp[i] != None:
            for num in nums:
                if i+num <= target:
                    newArr = dp[i] + [num]
                    if dp[i+num] and len(dp[i+num]) > len(newArr) or dp[i+num] == None: 
                        dp[i+num] = newArr
    return dp[target]


print("\tTabulation  Approach of best sum    7",bestSumTabulation(7,[5,3,4,7]))
print("\tTabulation  Approach of best sum    8",bestSumTabulation(8,[3,5,2]))
print("\tTabulation  Approach of best sum  100",bestSumTabulation(100,[3,4,25,2]))
print("\tTabulation  Approach of best sum 6249",bestSumTabulation(6249,[186,419,83,408]))
print("\tTabulation  Approach of best len   20",len(bestSumTabulation(6249,[186,419,83,408])))