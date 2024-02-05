class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stck = []
        p = 0
        for i in range(len(pushed)):
            stck.append(pushed[i])
            while p < len(popped) and stck and stck[-1] == popped[p]:
                stck.pop()
                p += 1
        return not stck

sol = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
ExpectedOutput = True
Output = sol.validateStackSequences(pushed, popped) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
