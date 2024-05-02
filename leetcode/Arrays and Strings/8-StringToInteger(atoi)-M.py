class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        # Variables for the result, the sign of the number, and the starting index
        res = 0
        sign = 1
        i = 0
        n = len(s)

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # If all characters were whitespace
        if i == n:
            return 0

        # Check the sign of the number
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Convert the following digits to an integer
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        # Apply the sign to the result
        res *= sign
        
        res = min(res, 2 ** 31 - 1)
        res = max(-(2 ** 31), res)
        return res

s = "   -042ab354"
ExpectedOutput = -42
sol = Solution()
Output = sol.myAtoi(s) 
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is:O(N)\n" )
