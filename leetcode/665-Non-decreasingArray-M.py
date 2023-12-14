class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        changed = False
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            elif changed:
                return False
            elif i == 0 or nums[i+1] >= nums[i - 1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True
        return True 

        

sol = Solution() 
nums = [4,2,1]
ExpectedOutput = False
Output = sol.checkPossibility(nums)
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )