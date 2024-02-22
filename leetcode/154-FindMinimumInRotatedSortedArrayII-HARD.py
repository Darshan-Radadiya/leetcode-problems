class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:

            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            mid = (l + r) // 2
            res = min(res,nums[mid])
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
            else: # nums[mid] == nums[l]
                l += 1
    
        return res
sol = Solution()
nums = [2,2,2,0,1]
ExpectedOutput = 0
Output = sol.findMin(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(log n) AND Space Complexity is: O(1)\n" )

