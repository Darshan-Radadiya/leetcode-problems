class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for i in range(n):
            res += ((ord(columnTitle[i])-ord('A')) + 1) * (26 ** (n-i-1))
        return res
        
        # or

        n = len(columnTitle)
        res = 0
        for i in range(n):
            res = res * 26
            res += ord(columnTitle[i]) - ord("A") + 1
        return res

sol = Solution()
s = "ADERLO" 
ExpectedOutput = 13809655
Output = sol.titleToNumber(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
