from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def checkThreeOdds(left, right):
            currSize = 0
            while left < right:
                if arr[left] % 2 != 0:
                    left += 1
                    currSize += 1
                elif currSize != 3:
                    return False
                if currSize == 3:
                    return True
            
        for i,ele in enumerate(arr):
            if ele % 2 != 0:
                if checkThreeOdds(i, len(arr)):
                    return True
        return False

sol = Solution()
nums = [1,2,34,3,4,5,7,23,12]
ExpectedOutput = True
Output = sol.threeConsecutiveOdds(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
