class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for n in nums:
            if n > 0:
                product *= 1
            elif n == 0:
                return 0
            else:
                product *= -1
        return product


sol = Solution()
nums = [-1,-2,-3,-4,3,2,1]
ExpectedOutput = 1
Output = sol.arraySign(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
