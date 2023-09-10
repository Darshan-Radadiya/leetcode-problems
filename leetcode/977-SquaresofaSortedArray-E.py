class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)

        while left <= right:
            if nums[left] < 0:
                nums[left] *= -1
            if nums[right] < 0:
                nums[right] *= -1
            if nums[left] > nums[right]:
                res[right - left] = nums[left] ** 2
                left += 1
            else:
                res[right - left] = nums[right] ** 2
                right -= 1
        return res

        

sol = Solution()
nums = [-4,-1,0,3,10]
ExpectedOutput = [0,1,9,16,100]
Output = sol.sortedSquares(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n) \n" )

        