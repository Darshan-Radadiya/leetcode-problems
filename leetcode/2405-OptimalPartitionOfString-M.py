class Solution:
    def partitionString(self, s: str) -> int:
        subStrCharSet = set()
        l, r, res = 0, 0, 1
        while r < len(s):
            if s[r] in subStrCharSet:
                l = r
                res += 1
                subStrCharSet = set()
            subStrCharSet.add(s[l])
            r += 1
        return res

sol = Solution()
s = "abacaba"
ExpectedOutput = 4
Output = sol.partitionString(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )