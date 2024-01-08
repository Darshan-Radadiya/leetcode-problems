class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            count = 1
            while p2+1 < len(nums) and nums[p2] == nums[p2+1]:
                p2 += 1
                count += 1
            for i in range(min(2,count)):
                nums[p1]=nums[p2]
                p1 += 1
            p2 += 1
            
        return nums[:p1]
    
sol = Solution()
nums = [0,0,0,0,1,2,2,3,3,3,3,5,5,5,6,7,7,7,8,9]
ExpectedOutput = [0, 0, 1, 2, 2, 3, 3, 5, 5, 6, 7, 7, 8, 9]
Output = sol.removeDuplicates(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n) and Space O(1)\n" )
