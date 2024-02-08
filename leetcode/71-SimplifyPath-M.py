class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ""
        stack = []

        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack: 
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c 

        return "/"+"/".join(stack)

        # stack = []

        # for i in path.split("/"):
        #     #  if i == "/" or i == '//', it becomes '' (empty string)

        #     if i == "..":
        #         if stack:
        #             stack.pop()
        #     elif i == "." or i == '':
        #         # skip "." or an empty string
        #         continue
        #     else:
        #         stack.append(i)

        # res = "/" + "/".join(stack)
        # return res
    
sol = Solution()
path = "/home//foo/"
ExpectedOutput = "/home/foo"
Output = sol.simplifyPath(path) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )