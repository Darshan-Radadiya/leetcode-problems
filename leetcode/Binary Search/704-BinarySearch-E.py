class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1

sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
ExpectedOutput = 4
Output = sol.search(nums, target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log n)\n" )
