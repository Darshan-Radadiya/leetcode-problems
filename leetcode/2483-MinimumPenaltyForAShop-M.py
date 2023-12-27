class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefixSumOfN = [0]*(n+1)
        postfixSumOfY = [0]*(n+1)
        
        for i in range(1, n+1):
            prefixSumOfN[i] = prefixSumOfN[i-1]
            if customers[i-1] == 'N':
                prefixSumOfN[i] += 1
    
        for i in range(n-1, -1, -1):
            postfixSumOfY[i] = postfixSumOfY[i+1]
            if customers[i] == 'Y':
                postfixSumOfY[i] += 1
        p, idx = float("inf"), 0
        for i in range(n+1):
            curr_p = prefixSumOfN[i] + postfixSumOfY[i] 
            if curr_p < p:
                p = curr_p
                idx = i
        return idx

sol = Solution()
s = "YYNYNYYNNYNYYYNNNYYYN"
ExpectedOutput = 14
Output = sol.bestClosingTime(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) AND Space Complexity is: O(n)\n" )
