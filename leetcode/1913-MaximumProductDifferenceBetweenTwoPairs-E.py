class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        
        currMin = min(nums) 
        nums.remove(currMin)
        currMax = max(nums)
        nums.remove(currMax)

        return (currMax * max(nums)) - (currMin *  min(nums))

sol = Solution()
nums = [4,2,5,9,7,4,8]
ExpectedOutput = 64
Output = sol.maxProductDifference(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
