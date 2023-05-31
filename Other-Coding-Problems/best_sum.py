# give array and number find the combination of number that can add up to given number with minimum combinations.
# O(m*n)


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

print(bestSum(7,[5,3,4,7],{}))
print(bestSum(100,[5,3,4,25],{}))