class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPointer = 0
        for nonZeroPointer in range(len(nums)):
            if nums[nonZeroPointer] != 0 and nums[zeroPointer] == 0:
                nums[zeroPointer], nums[nonZeroPointer] = nums[nonZeroPointer], nums[zeroPointer]
            if nums[zeroPointer] != 0:
                zeroPointer += 1
        return nums
sol = Solution()
nums = [1,0,1]
ExpectedOutput = [1,1,0]
Output = sol.moveZeroes(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n)\n" )
