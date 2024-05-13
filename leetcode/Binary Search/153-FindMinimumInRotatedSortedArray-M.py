class Solution:
    def findMin(self, nums):

        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
    
        return res

sol = Solution()
nums = [3,4,5,1,2]
Output = 1

# nums = [11,13,15,17]
# Output = 11
print("Expected Output:", Output)
print("Output: ", sol.findMin(nums))