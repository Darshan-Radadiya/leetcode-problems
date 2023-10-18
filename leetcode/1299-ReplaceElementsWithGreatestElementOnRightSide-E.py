class Solution:
    def replaceElements(self, nums: list[int]) -> list[int]:
        maximum = -1
        n = len(nums) - 1
        for i in range( n , -1, -1):
            currMaximum = max(maximum,nums[i])
            nums[i] = maximum
            maximum = currMaximum
        return nums
        

sol = Solution()
nums = [17,18,5,4,6,1]
ExpectedOutput = [18,6,6,6,1,-1]
Output = sol.replaceElements(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
