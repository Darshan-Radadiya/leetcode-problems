from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        temp = -1
        firstTimeZero = True
        for r in range(len(nums)):
            if nums[r] != 1: 
                if not firstTimeZero:
                    res = max(r - l, res)
                    l = temp + 1
                    temp = r
                else:
                    temp = r
                    firstTimeZero = False
                
        return max(res, r - l +  1)

sol = Solution()
nums = [1,0,1,1,1,0,0,0,0,1] 
ExpectedOutput = 5
Output = sol.findMaxConsecutiveOnes(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
