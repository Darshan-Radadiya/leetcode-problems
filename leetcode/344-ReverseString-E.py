class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
        return s
sol = Solution()
s = ["H","a","n","n","a","h"]
ExpectedOutput = ["h","a","n","n","a","H"] 
Output = sol.reverseString(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n/2)\n" )
