class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p1 = 1
        for p2 in range(1,len(nums)):
            if nums[p2] != nums[p2-1]:
                nums[p1] = nums[p2]
                p1 += 1
        return p1
    
sol = Solution()
nums = [0,0,0,0,1,2,2,3,3,3,3,5,5,5,6,7,7,7,8,9]
ExpectedOutput = 9
Output = sol.removeDuplicates(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n) and Space O(1)\n" )
