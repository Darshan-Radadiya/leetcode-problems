class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            c += n%2
            n = n >> 1
        return c

        #OR
        # count = 0
        # while n:
        #     n &= n-1
        #     count += 1
        # return res

sol = Solution()
n = 0b1011
ExpectedOutput = 3
Output = sol.hammingWeight(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(1)\n" )
