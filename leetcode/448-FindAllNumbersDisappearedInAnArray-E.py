class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res = []
        for n in nums:
            i = abs(n) - 1
            nums[i] = abs(nums[i]) * -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

sol = Solution()
nums = [4,3,2,7,8,2,3,1]
ExpectedOutput = [5,6]
Output = sol.pivotIndex(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
