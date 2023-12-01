class Solution:
    def largestNumber(self, nums: list[int]) -> str:
       # 9, 3, 30, 90, 5, 34   # 990534330

       nums = [str(n) for n in nums]

       for i in range(len(nums)):
           for j in range(i, len(nums)):
               if nums[i]+nums[j] > nums[j]+nums[i]:
                   continue
               else:
                   nums[i], nums[j] = nums[j], nums[i]
        
       ans = ''.join(nums)
       return 0 if int(ans) == 0 else ans

sol = Solution()
num = [9, 3, 30, 90, 5, 34]
ExpectedOutput = "990534330"
Output = sol.largestNumber(num) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2) in worst case and Space Complexity O(1)\n" )
