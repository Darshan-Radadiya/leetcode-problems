class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        def binary_search(currow, target):
            left = 0
            right = len(currow) - 1

            while left <= right:
                mid = left + ((right - left) // 2)
                if target == currow[mid]:
                    return True
                elif currow[mid] > target:
                    right = mid - 1
                elif currow[mid] < target:
                    left = mid + 1
            return False
        
        rowcount = len(matrix)
        currrow = 0
        while currrow != rowcount:
            print("matrix[currrow][-1]", matrix[currrow][-1])
            if matrix[currrow][-1] == target:
                return True
            elif matrix[currrow][-1] > target:
                return binary_search(matrix[currrow], target)
            else:
                currrow += 1
        return False
    

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
ExpectedOutput = True
Output = sol.searchMatrix(matrix, target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log M * N)\n" )
