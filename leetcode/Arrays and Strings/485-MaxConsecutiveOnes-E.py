from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] != 1:
                res = max(r - l, res)
                l = r + 1
        return max(res, r - l +  1)

sol = Solution()
nums = [1,0,1,1,1,0,0,0,0,1] 
ExpectedOutput = 3
Output = sol.findMaxConsecutiveOnes(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
