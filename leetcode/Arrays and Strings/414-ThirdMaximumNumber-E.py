from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax, secondMax, thirdMax = (-1, False), (-1, False), (-1, False)
        for ele in nums:
            if firstMax[1] and firstMax[0] == ele or secondMax[1] and secondMax[0] == ele or thirdMax[1] and thirdMax[0] == ele:
               continue

            if not firstMax[1] or firstMax[0] <= ele:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = (ele, True)
            
            elif not secondMax[1] or secondMax[0] <= ele:
                thirdMax = secondMax
                secondMax = (ele, True)
            
            elif not thirdMax[1] or thirdMax[0] <= ele:
                thirdMax = (ele, True)
        
        if not thirdMax[1]:
            return firstMax[0]
        return thirdMax[0]

sol = Solution()
nums = [2,2,3,1] 
ExpectedOutput = 1
Output = sol.thirdMax(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
