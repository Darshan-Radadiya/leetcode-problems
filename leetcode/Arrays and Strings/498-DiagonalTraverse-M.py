from collections import defaultdict
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])
        diagonalDict = defaultdict(list)
		# key - diagonal elements have the same r + c value.
        for r in range(R):
            for c in range(C):
                diagonalDict[r+c].append(mat[r][c])
        ans = []
        for i, value in enumerate(diagonalDict.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        return ans

sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
ExpectedOutput = [1,2,4,7,5,3,6,8,9]
Output = sol.findDiagonalOrder(mat) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m*n)\n" )
