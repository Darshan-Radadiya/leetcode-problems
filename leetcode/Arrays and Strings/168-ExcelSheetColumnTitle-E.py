class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            temp = (columnNumber - 1) // 26 
            currChar = (columnNumber - 1) % 26
            res = chr((currChar + ord('A'))) + res
            columnNumber = temp
        return res

sol = Solution()
columnNumber = 2147483647
ExpectedOutput = "FXSHRXW"
Output = sol.convertToTitle(columnNumber) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(log base 26 n == log n)\n" )
