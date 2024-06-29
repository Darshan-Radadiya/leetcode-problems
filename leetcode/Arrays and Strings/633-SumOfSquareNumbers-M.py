from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while a <= b:
            if a*a + b*b == c:
                return True
            if a*a + b*b > c:
                b -= 1
            else:
                a += 1
        return False

sol = Solution()
c = 5
ExpectedOutput = True
Output = sol.judgeSquareSum(c) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(sqrt(c)) and O(1)\n" )
