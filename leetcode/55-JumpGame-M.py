class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0  
        for i in range(len(nums)):
            if i > max_reach: 
                return False
            max_reach = max(max_reach, i + nums[i])  
        return True
    
sol = Solution()
nums = [2,0,0]
ExpectedOutput = True
Output = sol.canJump(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
