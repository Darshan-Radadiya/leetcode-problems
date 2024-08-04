from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        i = 0
        # Going upward
        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == n-1:
            return False
        
        #  Going Downward
        while i + 1 < n and arr[i] > arr[i+1]:
            i += 1
        
        return i == n - 1

sol = Solution()
nums = [0,1,2,3,2,1,0]
ExpectedOutput = True
Output = sol.validMountainArray(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
