class Solution:
    def isValid(self, s: str) -> bool:

        Map = { "}":"{", "]":"[", ")":"(" }
        stack = []

        for b in s:
            if b in Map:
                if stack and stack[-1] == Map[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return True if not stack else False


sol = Solution()
s = "()[]{}"
ExpectedOutput = True
Output = sol.isValid(s)
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is:O(N) and Space is O(N)\n" )
