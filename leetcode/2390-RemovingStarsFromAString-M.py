class Solution(object) :
    def removeStars(self, s) :
        res = []
        for c in s :
            if res and c == '*':
                res.pop()
            else:
                res.append(c)
        return ''.join(res)
    
sol = Solution()
s = "leet**cod*e"
ExpectedOutput = "lecoe"
Output = sol.removeStars(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
