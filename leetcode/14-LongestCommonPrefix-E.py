class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        if "" in strs:
            return res 
        elif len(strs) == 1:
            return strs[0]
        else:
            for n in range(len(strs[0])):
                for s in strs:
                    if n == len(s) or s[n] != strs[0][n]:
                        return res
                res += strs[0][n]
        return res

        

sol = Solution()
strs = ["fl","f"]
ExpectedOutput = "f"
Output = sol.longestCommonPrefix(strs) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m*n)\n" )
