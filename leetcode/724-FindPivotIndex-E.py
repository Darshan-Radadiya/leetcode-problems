class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        l, r = 0, sum(nums)
        for i in range(len(nums)):
            l += nums[i]
            r -= nums[i]
            if l == (r + nums[i]):
                return i
        return -1   

sol = Solution()
nums = [1,7,3,6,5,6]
ExpectedOutput = 3
Output = sol.pivotIndex(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
