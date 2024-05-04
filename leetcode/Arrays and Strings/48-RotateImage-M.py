class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
            Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1 
        return matrix


        #    Printing Matrix
            # for r in matrix:
            #     print()
            #     for c in r:
            #         print(c, end =" ")                



        


sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 1 2 3    # 7 4 1 
# 4 5 6    # 8 5 2
# 7 8 9    # 9 6 3
ExpectedOutput = [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 5  1  9  11   # 15 13 2  5
# 2  4  8  10   # 14 3  4  1
# 13 3  6  7    # 12 6  8  9
# 15 14 12 16   # 16 7 10 11
ExpectedOutput = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Output = sol.rotate(matrix) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2) and Space is O(1)\n" )