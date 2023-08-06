class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask) 


sol = Solution()
a = 100
b = 2000
ExpectedOutput = 2100
Output = sol.getSum(a, b) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time & Space Complexity is: O(1)\n" )
