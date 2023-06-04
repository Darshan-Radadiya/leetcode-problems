# Given a target and wordBank. 
# return all possible combinations of word from wordBank to generate the target.
# for ex.
# target = Purple
# wordBank = ['purp', 'p', 'ur' , 'le', 'purpl']
# expectedOutput = [ [purp, le], [p, ur, p, le] ]

def allConstruct(target, wordBank,memo):
    results = []
    if target in memo: return memo[target]
    if target == '': return [[]]

    for word in wordBank:
        if target[:len(word)] == word:
            suffix = target[len(word):]
            combinations = allConstruct(suffix, wordBank,memo)
            for combination in combinations:
                results.append([word] + combination)
    memo[target] = results
    return results


def allConstructTabulation(target, wordBank):
    dp = [[] for _ in range(len(target) + 1)]
    dp[0] = [[]]

    for i in range(len(target) + 1):
        if dp[i]:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    newCombinations = [combination + [word] for combination in dp[i]]
                    dp[i+len(word)].extend(newCombinations)

    return dp[len(target)]



print(allConstruct('purple',['purp', 'p', 'ur' , 'le', 'purpl'],{} ))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz',['a', 'aa', 'aaa' , 'aaaa', 'aaaaa'], {} ))
print( " '\033[1m' Time complexity is exponential O(n^m) for both approach and space is O(m(height of the tree)) for memo and O(n^m) for Tabulation'\033[0m' ")