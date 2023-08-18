class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        valid_operator = ['+', '-', '*', '/']
        for t in tokens:
            if t in valid_operator:
                res = 0
                operand1 = stack.pop()
                operand2 = stack.pop()
                if t == "+":
                    res = (operand2) + (operand1)
                elif t == "-":
                    res = (operand2) - (operand1) 
                elif t == "*":
                    res = (operand2) * (operand1) 
                elif t == "/":
                    res = int((operand2) / (operand1))
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]

sol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ExpectedOutput = 22
Output = sol.evalRPN(tokens) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
