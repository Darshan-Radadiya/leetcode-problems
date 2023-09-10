class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left += 1
                res = mid + 1
            else:
                right -= 1
        return res

sol = Solution()
nums = [1,3,5,6]
target = 7
ExpectedOutput = 4
Output = sol.searchInsert(nums, target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log(n) \n" )