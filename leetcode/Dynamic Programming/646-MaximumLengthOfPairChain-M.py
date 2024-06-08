from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Optimal Approach O( n log n)
        # Sort pairs in ascending order based on the second element.
        pairs.sort(key=lambda x: x[1])
        curr = float('-inf')
        ans = 0

        for pair in pairs:
            if pair[0] > curr:
                ans += 1
                curr = pair[1]
        return ans
        

        pairs = sorted(pairs)

        # Top down O(n^2)
        n = len(pairs)
        memo = [[-1] * (n+1)] * n
        def solve(i, prevIdx):
            if i >= n:
                return 0
            if memo[i][prevIdx+1] != -1:
                return memo[i][prevIdx+1]
            take = 0
            if prevIdx == -1 or pairs[i][0] > pairs[prevIdx][1]:
                take = 1 + solve(i+1, i)
            skip = solve(i+1, prevIdx)
            memo[i][prevIdx+1] = max(take, skip)
            return memo[i][prevIdx+1]
        return solve(0, -1)

        #  bottom up approach O(n ^ 2)
        memo = [1] * (len(pairs) + 1)

        for i in range(1,len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    memo[i] = max(memo[i], (memo[j]+1))
        return max(memo)
            

sol = Solution()
pairs = [[1,2],[7,8],[4,5]]
ExpectedOutput = 3
Output = sol.findLongestChain(pairs) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2)\n" )
