class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def removeDuplicateStars(p):
            newP = []
            for char in p:
                if not newP or char != '*':
                    newP.append(char)
                elif newP[-1] != "*":
                    newP.append(char)
            return "".join(newP)

        def helper(s, p):
            if (s,p) in dp:
                return dp[(s,p)]
            
            if s == p or p == "*":
                dp[(s,p)] = True
            elif p == "" or s == "":
                dp[(s,p)] = False
            elif p[0] == s[0] or p[0] == "?":
                dp[(s,p)] = helper(s[1:],p[1:])
            elif p[0] == "*":
                dp[(s,p)] = helper(s, p[1:]) or helper(s[1:], p)
            else:
                dp[(s,p)] = False
            return dp[(s,p)]
        dp = {}
        p = removeDuplicateStars(p)
        return helper(s,p)
#  space and time = O(s * p (s+p)) and O(s*p)

s = "cbbdac"
p = "?b*bd*c"
sol = Solution()
Output = sol.isMatch(s, p)
ExpectedOutput = True
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(S * P * (S+P))\n" )

