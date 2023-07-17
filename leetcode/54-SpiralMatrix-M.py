class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while left < right and top < bottom:
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top,bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
ExpectedOutput = [1,2,3,4,8,12,11,10,9,5,6,7]
Output = sol.spiralOrder(matrix) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m*n) and Space is O(1)\n" )