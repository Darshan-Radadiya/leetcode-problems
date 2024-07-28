from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxEleIdx = 0
        secondMax = float('-inf')
        
        for i in range(1, len(nums)):
            if nums[i] > nums[maxEleIdx]:
                secondMax = nums[maxEleIdx]
                maxEleIdx = i
            elif nums[i] > secondMax:
                secondMax = nums[i]
        
        if nums[maxEleIdx] >= 2 * secondMax:
            return maxEleIdx
        else:
            return -1

sol = Solution()
nums = [3,6,1,0]
ExpectedOutput = 1
Output = sol.dominantIndex(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
