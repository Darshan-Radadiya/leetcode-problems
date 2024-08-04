from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1
        return res
    
        # or
        # Modular Approach - 
        res = 0
        for n in nums:
            currLen = 0
            while n:
                currLen += 1
                n //= 10
            if currLen % 2 == 0:
                res += 1
            
        return res

sol = Solution()
numRows = [555,901,482,1771]
ExpectedOutput = 1
Output = sol.findNumbers(numRows) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log m) and Space is O(log m)\n" )
