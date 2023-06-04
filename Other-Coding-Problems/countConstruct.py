def countConstructTabulationApproach(s: str, wordDict: list[str]) -> bool:
    dp = [0]*(len(s)+1)
    dp[0] = 1
    for ic in range(len(s)):
        for word in wordDict:
            if s[ic:len(word)+ic] == word:
                    dp[len(word)+ic] += dp[ic]
    return dp[len(s)]



s = "purple"
wordDict = ["purp","p","ur","le","purpl"]
print("\t Output is\t", countConstructTabulationApproach(s,wordDict))

print("Time Complexity for Tabulation is: O(N*m^2(wordDict len))\n" )
print("Space Complexity for Tabulation is: O(M)\n" )