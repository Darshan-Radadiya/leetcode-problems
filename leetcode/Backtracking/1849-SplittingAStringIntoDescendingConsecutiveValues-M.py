class Solution:
    def backtrack(self, i, s, prevVal):
        if i == len(s):
            return True
        for j in range(i, len(s)):
            val = int(s[i : j+1])
            if val+1 == prevVal and self.backtrack(j+1, s, val):
                return True
        return False
    def splitString(self, s: str) -> bool:
        res = []
        for i in range(len(s) - 1):
            prevVal = int(s[:i+1])
            if self.backtrack(i+1, s, prevVal):
                return True
        return False

nums = "00504321"
sol = Solution()
Output = sol.splitString(nums)
ExpectedOutput = True
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^n) \n" )
