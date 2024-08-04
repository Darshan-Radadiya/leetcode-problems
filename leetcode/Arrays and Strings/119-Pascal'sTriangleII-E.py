from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []
        for i in range(rowIndex+1):
            curr = [1] * (i+1)
            for j in range(1,i):
                curr[j] = prev[j] + prev[j-1]
            prev = curr
        return curr

sol = Solution()
numRows = 5
ExpectedOutput = [1, 5, 10, 10, 5, 1] 
Output = sol.getRow(numRows) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space is O(1)\n" )
