class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    right = mid - 1
                elif mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                    left = mid + 1
                else:
                    return nums[mid]
            else: 
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
                    right = mid - 1
                else:
                    return nums[mid]



sol = Solution()
nums = [3,3,7,7,10,11,11]
ExpectedOutput = 10
Output = sol.singleNonDuplicate(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log(n) \n" )

        