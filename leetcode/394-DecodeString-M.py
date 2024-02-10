class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                currStr = ""
                while stack[-1] != "[":
                    currStr = stack.pop() + currStr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                stack.append(int(k) * currStr)
        return "".join(stack)
    
s = "3[a2[c]]"
ExpectedOutput = "accaccacc"
sol = Solution()
Output = sol.decodeString(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
