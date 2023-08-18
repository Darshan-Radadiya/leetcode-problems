class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_bracket, close_bracket):

            if open_bracket == close_bracket == n:
                res.append("".join(stack))
                return

            if open_bracket < n:
                stack.append('(')
                backtrack(open_bracket + 1, close_bracket)
                stack.pop()
            
            if close_bracket < open_bracket:
                stack.append(')')
                backtrack(open_bracket, close_bracket + 1)
                stack.pop()

        backtrack(0,0)
        return res

sol = Solution()
n = 3
ExpectedOutput = ["((()))","(()())","(())()","()(())","()()()"]
Output = sol.generateParenthesis(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
