class Solution:
    def maxScore(self, s: str) -> int:
        noOfOne = noOfZero = ans = 0
        for i in s:
            if i == '1':
                noOfOne += 1
        for i in range(len(s)-1):
            if s[i] == '1':
                noOfOne -= 1
            else:
                noOfZero += 1
            ans = max(noOfZero + noOfOne, ans)
        return ans

sol = Solution()
s = "011101"
ExpectedOutput = 5
Output = sol.maxScore(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(1)\n" )
