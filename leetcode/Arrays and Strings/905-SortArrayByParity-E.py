from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        writePointer = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[writePointer], nums[i] = nums[i], nums[writePointer]
                writePointer += 1
        return nums

sol = Solution()
nums = [3,1,2,4]
ExpectedOutput = [2, 4, 3, 1] 
Output = sol.sortArrayByParity(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )

