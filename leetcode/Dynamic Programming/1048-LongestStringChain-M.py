from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # O(n^2) Bottom Up
        def isPredecessor (prevWord, currWord):
            N = len(prevWord)
            M = len(currWord)
            if N >= M or M - N != 1:
                return False
            i, j = 0, 0
            while i < N and j < M:
                if prevWord[i] == currWord[j]:
                    i += 1
                j += 1
            return i == N

        words.sort(key = lambda word: len(word))
        memo = [1] * (len(words) + 1)
        for i in range(1,len(words)):
            for j in range(i):
                if isPredecessor(words[j],words[i]):
                    memo[i] = max(memo[i], (memo[j]+1))
        return max(memo)


        # O(n ^2) Top Down
        n = len(words)
        words.sort(key = lambda word: len(word))
        memo = [[-1] * (n+1)] * n

        def isPredecessor (prevWord, currWord):
            N = len(prevWord)
            M = len(currWord)
            if N >= M or M - N != 1:
                return False
            i, j = 0, 0
            while i < N and j < M:
                if prevWord[i] == currWord[j]:
                    i += 1
                j += 1
            return i == N

        def solve(i, prevIdx):
            if i >= n:
                return 0
            if memo[i][prevIdx+1] != -1:
                return memo[i][prevIdx+1]
            take = 0
            if prevIdx == -1 or isPredecessor(words[prevIdx], words[i]):
                take = 1 + solve(i+1, i)
            skip = solve(i+1, prevIdx)

            memo[i][prevIdx+1] = max(take, skip)
            return memo[i][prevIdx+1]

        return solve(0, -1)


sol = Solution()
words = ["xbc","pcxbcf","xb","cxbc", "pcxbc"]
ExpectedOutput = 5
Output = sol.longestStrChain(words) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2)\n" )
