class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                currRes = [1]
                for j in range(len(res[i - 1]) - 1):
                    currRes.append(res[i-1][j]+res[i-1][j+1])
                currRes.append(1)
                res.append(currRes)
        return res


sol = Solution()
numRows = 5
ExpectedOutput = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Output = sol.generate(numRows) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m*n)\n" )
