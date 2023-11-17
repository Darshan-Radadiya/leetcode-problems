class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ## Modified Bucket Sort
        left, right = 0, len(nums)-1
        i = 0 
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

sol = Solution()
nums = [2,0,2,1,1,0]
ExpectedOutput = [0,0,1,1,2,2]
Output = sol.sortColors(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(1)\n" )
