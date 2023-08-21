class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)
         
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t, i])
        return res


sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
ExpectedOutput = [1,1,4,2,1,1,0,0]
Output = sol.dailyTemperatures(temperatures) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n)\n" )
