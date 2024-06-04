class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # O( N * M ) Bottom up
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j - 1]
                    delete = dp[i - 1][j]
                    replace = dp[i - 1][j - 1]
                    dp[i][j] =  1 + min(insert, delete, replace)
        return dp[n][m]

        # O(N * M) Top-down approach from the last index
        n, m = len(word1), len(word2)
        memo = [[None for _ in range(m + 1)] for _ in range(n + 1)]

        def solve(i, j):
            # If word1 is exhausted (i == 0), we need to insert all remaining characters of word2 (j characters).
            if i == 0:
                return j

            # If word2 is exhausted (j == 0), we need to delete all remaining characters of word1 (i characters).
            if j == 0:
                return i

            # Check if the result is already computed and stored in memo
            if memo[i][j] is not None:
                return memo[i][j]

            # If the characters match, move to the next pair of characters
            if word1[i - 1] == word2[j - 1]:
                memo[i][j] = solve(i - 1, j - 1)
            else:
                # Compute the costs of insert, delete, and replace operations
                insert = 1 + solve(i, j - 1)
                delete = 1 + solve(i - 1, j)
                replace = 1 + solve(i - 1, j - 1)
                # Take the minimum of the three operations
                memo[i][j] = min(insert, delete, replace)

            return memo[i][j]

        return solve(n, m)



        # O( N * M ) Top Down from 0th index.
        n, m = len(word1), len(word2)
        memo = {}
        def solve(i, j):
            #  w1 = ab and w2 = abc so if ab done then we need to add 'c' in w1 to make both same so n - j
            if i == n:
                return m - j

            #  w1 = abc and w2 = ab so if ab w2 done then we need to delete 'c' from w1 to make both same so m - i
            if j == m :
                return n - i

            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i] == word2[j]:
                return solve(i+1, j+1)
            else:
                insert = 1 + solve(i, j+1)
                delete = 1 + solve(i+1, j)
                replace = 1 + solve(i+1, j+1)
                memo[(i,j)] = min(insert, delete, replace)

            return memo[(i,j)]
        
        return solve(0,0)

sol = Solution()
text1 = "abac"
text2 = "cab" 
ExpectedOutput = 3
Output = sol.minDistance(text1,text2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(n * m)\n" )