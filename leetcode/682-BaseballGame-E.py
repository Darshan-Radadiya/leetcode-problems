class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score = []
        for i in range(len(operations)):
            op = operations[i]
            if op == 'C':
                score.remove(score[len(score)-1])
            elif op == '+':
                score.append(score[len(score)-1] +score[len(score)-2])
            elif op == 'D':
                score.append(score[len(score)-1]*2)
            else:
                score.append(int(op))
        return sum(score)
    
sol = Solution()
operations = ["5","-2","4","C","D","9","+","+"]
ExpectedOutput = 27
Output = sol.calPoints(operations) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
