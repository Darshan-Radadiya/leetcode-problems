from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^=n
        return xor

sol = Solution()
nums = [4,1,2,1,2]
ExpectedOutput = 4
Output = sol.singleNumber(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and space O(1)\n" )
