class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPointer, nonZeroPointer = 0, 0
        for nonZeroPointer in range(len(nums)):
            if nums[nonZeroPointer] != 0 and nums[zeroPointer] == 0:
                nums[zeroPointer], nums[nonZeroPointer] = nums[nonZeroPointer], nums[zeroPointer]
                nonZeroPointer += 1
            if nums[zeroPointer] != 0:
                zeroPointer += 1
        return nums
sol = Solution()
nums = [0,1,0,3,12]
ExpectedOutput = [1,3,12,0,0]
Output = sol.moveZeroes(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n)\n" )
